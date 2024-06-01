import re

from markup_converter.readers.base_parser import BaseParser
from markup_converter.readers.state import BlockState
from markup_converter.readers.utils import (
    convert_all_tabs_to_spaces,
    convert_leading_tabs_to_spaces,
    unescape_char,
)

_BLOCK_QUOTE_TRIM = re.compile(r'^ ?', flags=re.M)
_BLOCK_QUOTE_LEADING = re.compile(r'^ *>', flags=re.M)

_LINE_BLANK_END = re.compile(r'\n[ \t]*\n$')

_STRICT_BLOCK_QUOTE = re.compile(r'( {0,3}>[^\n]*(?:\n|$))+')

class BlockParser(BaseParser):
    GRAMMAR_RULES = {
        'blank_line': r'(^[ \t\v\f]*\n)+',
        'atx_heading': r'^ {0,3}(?P<level>#{1,6})(?!#+)(?P<atx_text>[ \t]*|[ \t]+.*?)$',
        'setext_heading': r'^ {0,3}(?P<sep>=|-){1,}[ \t]*$',
        'horizontal_rule': r'^ {0,3}((?:-[ \t]*){3,}|(?:_[ \t]*){3,}|(?:\*[ \t]*){3,})$',
        'block_quote': r'^ {0,3}>(?P<quote_text>.*?)$',
        'code_fenced': (
            r'^(?P<fnc_spaces> {0,3})(?P<fnc_marker>`{3,}|~{3,})'
            r'[ \t]*(?P<fnc_lang>.*?)$'
        ),
        'code_indent': (
            r'^(?: {4}| *\t)[^\n]+(?:\n+|$)'
            r'((?:(?: {4}| *\t)[^\n]+(?:\n+|$))|\s)*'
        ),
    }

    RULES_NAMES = [
        'code_fenced',
        'code_indent',
        'atx_heading',
        'setext_heading',
        'horizontal_rule',
        'blank_line',
        'block_quote',
        ]

    def __init__(self) -> None:
        super().__init__()

        self._methods = {
            rule: getattr(self, f'visit_{rule}') for rule in self.rules
        }
    
    def visit_blank_line(self, m: re.Match[str], state: BlockState) -> int:
        """
        Visit method for BlankLine.

        BlankLine is not present in AST, but still needed to 
        prevent reading empty lines as paragraphs.
        """
        state.blocks.append({'type': 'blank_line'})
        return m.end()
    
    def visit_atx_heading(self, m: re.Match[str], state: BlockState) -> int:
        """
        Visit method for ATX headings.

        # Header example
        """
        level = len(m.group('level'))
        text = m.group('atx_text').strip()
        
        # cases: # header ### -> text = header
        #        # header ### some -> text = header ### some
        if text:
            heading_text_regex = re.compile(r'(\s+|^)#+\s*$')
            text = heading_text_regex.sub('', text)

        header_id = text.lower().replace("#", "").replace(' ', '-')

        block = {
            'type': 'Heading', 
            'content': text,
            'level': level,
            'attrs': [['id', header_id], ["style", 'atx']]
            }
        state.append(block)
        return m.end() + 1

    def visit_setext_heading(self, m: re.Match[str], state: BlockState) -> int:
        """
        Visit method for Setext headings.

        Header example
        ==============
        """
        # setext heading are interpreted as para, so we need to change the last one
        if state.last_block and state.last_block['type'] == 'Para':
            state.last_block['type'] = 'Heading'

            level = 1 if m.group("sep").startswith('=') else 2
            header_text = state.last_block['content']
            header_id = header_text.strip().lower().replace("#", "").replace(' ', '-')

            state.last_block['level'] = level
            state.last_block['attrs'] = [
                ["id", header_id], ['style', 'setext']
            ]
            return m.end() + 1
        
        # it can match list and horizontal rule also
        # TODO: add list here
        regexs = self.compile_regex(['horizontal_rule'])
        match = regexs.search(state.parse_text, state.cursor_pos)
        if match:
            return self.get_parse_method(match, state)
        return None
    
    def visit_horizontal_rule(self, m: re.Match[str], state: BlockState) -> int:
        """
        Visit method for Horizontal Rule.

        ---
        """
        state.append({'type': 'HorizontalRule'})
        return m.end() + 1
    
    def visit_code_indent(self, m: re.Match[str], state: BlockState) -> int:
        """
        Visit method for Code Indent (4 spaces before code).

            print("Hello")
            print("World!")
        """
        # it can match part of Para also
        pos = state.append_para()
        if pos:
            return pos
        
        code = m.group(0)
        code = convert_leading_tabs_to_spaces(code)

        leading_spaces_regex = re.compile(r'^ {1,4}', flags=re.M)
        code = leading_spaces_regex.sub('', code)

        code = code.strip('\n')
        state.append({'type': 'CodeBlock', 'content': code, 'attrs': [['style', 'indented']]})
        return m.end()
    
    def _validate_fenced_lang(self, marker: str, lang: str) -> None:
        """
        Validate language for code block with marker `.
        """
        if lang and marker.startswith('`') and '`' in lang:
            raise ValueError(
                "Language for code block indented by " + 
                "backtics cannot contain backticks."
            )
    
    def _parse_code_and_end_pos(
            self, state: BlockState, end_pattern: re.Pattern[str], cursor_start: int
        ) -> tuple[str, int]:
        match = end_pattern.search(state.parse_text, cursor_start)
        if match:
            code = state.parse_text[cursor_start:match.start()]
            end_pos = match.end()
        else:
            code = state.parse_text[cursor_start:]
            end_pos = state.max_cursor_pos
        return code, end_pos
    
    def _trim_code_indent(self, code: str, indent_spaces: str) -> str:
        if not code or not indent_spaces:
            return code
        _trim_regex = re.compile('^ {0,' + str(len(indent_spaces)) + '}', re.M)
        return _trim_regex.sub('', code)
    
    def visit_code_fenced(self, m: re.Match[str], state: BlockState) -> int:
        """
        Visit method for Code Fenced.

        ``` python
        print("Hello, World!")
        ```
        """
        indent_spaces = m.group('fnc_spaces')
        delimiter = m.group('fnc_marker')
        language = m.group('fnc_lang')

        self._validate_fenced_lang(delimiter, language)

        end_regex = re.compile(
            r'^ {0,3}'
            + delimiter[0]
            + '{' + str(len(delimiter))
            + r',}[ \t]*(?:\n|$)', re.M
        )
        cursor_start = m.end() + 1

        code, end_pos = self._parse_code_and_end_pos(state, end_regex, cursor_start)

        code = self._trim_code_indent(code, indent_spaces)

        block = {
            'type': 'CodeBlock',
            'content': code,
            'attrs': [['style', 'fenced'], ['marker', delimiter[0]]]
        }
        if language:
            language = unescape_char(language)
            block['attrs'].append(['language', language.strip()])

        state.append(block)
        return end_pos

    def _process_quote(self, m: re.Match[str]) -> str:
        quote = m.group(0)
        quote = _BLOCK_QUOTE_LEADING.sub('', quote)
        quote = convert_leading_tabs_to_spaces(quote, 3)
        quote = _BLOCK_QUOTE_TRIM.sub('', quote)
        return quote

    def _is_previous_line_blank(self, quote: str) -> bool:
        if not quote.strip():
            return True
        else:
            return bool(_LINE_BLANK_END.search(quote))
    
    def _process_quote_no_marker(self, quote_text: str, state: BlockState) -> tuple[str, int]:
        is_prev_line_blank = False
        break_regex = self.compile_regex([
            'blank_line', 'horizontal_rule', 'code_fenced',
        ])

        end_position = None

        while state.cursor_pos < state.max_cursor_pos:
            match = _STRICT_BLOCK_QUOTE.match(state.parse_text, state.cursor_pos)
            if match:
                quote = self._process_quote(match)
                quote_text += quote
                state.cursor_pos = match.end()
                is_prev_line_blank = self._is_previous_line_blank(quote)
                continue

            if is_prev_line_blank:
                break

            match = break_regex.match(state.parse_text, state.cursor_pos)
            if match:
                end_position = self.get_parse_method(match, state)
                if end_position:
                    break

            pos = state.find_endline()
            line = state.get_text_before(pos)
            line = convert_leading_tabs_to_spaces(line, 3)
            quote_text += line
            state.cursor_pos = pos
        return quote_text, end_position

    def _get_block_quote(
        self, m: re.Match[str], state: BlockState
    ) -> tuple[str, int]:

        quote_text = m.group('quote_text') + '\n'
        quote_text = convert_leading_tabs_to_spaces(quote_text, 3)
        quote_text = _BLOCK_QUOTE_TRIM.sub('', quote_text)

        sc = self.compile_regex(['blank_line', 'code_indent', 'code_fenced'])
        require_marker = bool(sc.match(quote_text))

        state.cursor_pos = m.end() + 1

        end_position = None

        if require_marker:
            match = _STRICT_BLOCK_QUOTE.match(state.parse_text, state.cursor_pos)
            if match:
                quote = self._process_quote(match)
                quote_text += quote
                state.cursor_pos = match.end()
        else:
            quote_text, end_position = self._process_quote_no_marker(quote_text, state)

        return convert_all_tabs_to_spaces(quote_text), end_position

    def visit_block_quote(self, m: re.Match[str], state: BlockState) -> int:
        """
        Visit method for Block Quote.

        > This is a block quote.
        > ```
        > It can contain other blocks.
        > ```
        """

        quote_text, end_pos = self._get_block_quote(m, state)
        child = state.init_child_state(quote_text)
        if state.nesting_lvl >= 4:
            rules = list(self.rules)
            rules.remove('block_quote')
        else:
            rules = self.rules

        self.parse(child, rules)
        block = {'type': 'BlockQuote', 'children': child.blocks}
        if end_pos:
            state.insert_second_to_last(block)
            return end_pos
        state.append(block)
        return state.cursor_pos
    
    def _update_state(self, state: BlockState, new_pos: int) -> None:
        """
        Extracts text from the current cursor position to new_pos, 
        adds it as a paragraph to the state,
        and updates the cursor position.
        """
        text = state.get_text_before(new_pos)
        state.add_para(text)
        state.cursor_pos = new_pos

    def parse(self, state: BlockState, rules: list[str] = None) -> None:
        """
        Parse source Markdown text into blocks.
        Blocks are stored in the state with the following structure:
        {
            'type': str, 
            'content': str, 
            'attrs': dict
        }
        """
        if not rules:
            rules = self.rules
        regexs = self.compile_regex(rules)

        while state.cursor_pos < state.max_cursor_pos:
            match = regexs.search(state.parse_text, state.cursor_pos)
            if not match:
                break

            match_pos = match.start()
            if match_pos > state.cursor_pos:
                self._update_state(state, match_pos)

            new_pos = self.get_parse_method(match, state)
            if new_pos:
                state.cursor_pos = new_pos
            else:
                new_pos = state.find_endline()
                self._update_state(state, new_pos)

        if state.cursor_pos < state.max_cursor_pos:
            self._update_state(state, state.max_cursor_pos)