from typing import Any

from parsimonious import Grammar, NodeVisitor

from markup_converter.readers.markdown_block_parser import BlockParser
from markup_converter.readers.state import BlockState
from markup_converter.structure import block as block
from markup_converter.structure import content as content
from markup_converter.structure import document as document
from markup_converter.structure import inline as inline


def flatten(nested_list):
    if isinstance(nested_list, list):
        return [item for sublist in nested_list for item in flatten(sublist)]
    else:
        return [nested_list]


inline_grammar = Grammar(
    r"""
    inline = (emph / strong / content)+

    emph = "*" !space (inline_no_emph)+ "*"
    strong = "**" !space (inline_no_strong)+ "**"
    content = (space / word)

    space = spacechar+
    spacechar = " " / "\t"
    word = ~"[^\s]+"

    content_no_emph = (space / word_no_star)
    word_no_star = ~"[^\s*]+"
    inline_no_emph = strong / content_no_emph

    content_no_strong = (space / word_no_star_star)
    word_no_star_star = ~"[^\s**]+"
    inline_no_strong = emph / content_no_strong

    newline = "\n"
    """
)


class InlineVisitor(NodeVisitor):
    def visit_emph(self, node, visited_children):
        inlines = flatten(visited_children[2])
        return inline.Emph(inlines)

    def visit_content(self, node, visited_children):
        return visited_children

    def visit_space(self, _1, _2):
        return inline.Space()

    def visit_strong(self, node, visited_children):
        inlines = flatten(visited_children[2])
        return inline.Strong(inlines)

    def generic_visit(self, node, visited_children):
        method_name = "visit_" + node.expr_name
        method = getattr(self, method_name, None)
        if callable(method):
            return method(node, visited_children)
        elif method_name.startswith("visit_word"):
            return inline.Str(node.text)
        return visited_children or node


class MarkdownBlockReader:
    """
    Reads the text in the BlockState and parses it into blocks.
    """

    def __init__(self) -> None:
        self.parser = BlockParser()
        self.inline_parser = InlineVisitor()

    def _normalize_text(self, text: str) -> str:
        # in order to simplify newline rule
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        return text if text.endswith("\n") else text + "\n"

    def _parse_block(self, block_: dict[str, Any]) -> None:
        text = block_["content"].strip("\n")
        tree = inline_grammar.parse(text)
        res = self.inline_parser.visit(tree)
        flat_res = flatten(res)

        if block_["type"] == "Para":
            return block.Para(flat_res)
        elif block_["type"] == "Heading":
            attr = content.Attr(["", [], block_["attrs"]])
            return block.Header([block_["level"], attr, flat_res])

    def _parse_blocks(self, blocks: list[dict[str, Any]]):
        parsed_block = []
        for block_ in blocks:
            if block_["type"] == "blank_line":
                continue

            no_inline_block = self._parse_block_with_no_inline_processing(block_)
            if no_inline_block:
                parsed_block.append(no_inline_block)
                continue

            if "children" in block_:
                children = self._parse_blocks(block_["children"])
                parsed_block.append(self._construct_container(block_, children))
            else:
                parsed_block.append(self._parse_block(block_))
        return parsed_block

    def _construct_container(self, block_: dict[str, Any], children: list[block.Block]) -> block.Block:
        container_blocks = {
            "BlockQuote": block.BlockQuote,
        }
        if block_["type"] in container_blocks:
            return container_blocks[block_["type"]](children)

    def _parse_block_with_no_inline_processing(self, block_: dict[str, Any]) -> block.Block:
        content_attr_blocks = {
            "CodeBlock": block.CodeBlock,
        }
        no_arg_blocks = {
            "HorizontalRule": block.HorizontalRule,
        }
        if block_["type"] in no_arg_blocks:
            return no_arg_blocks[block_["type"]]()
        elif block_["type"] in content_attr_blocks:
            content_ = block_["content"]
            attr = content.Attr(["", [], block_["attrs"]])
            return content_attr_blocks[block_["type"]]([attr, content_])

    def parse(self, text: str) -> document.Document:
        state = BlockState()

        text = self._normalize_text(text)
        state.init_parse_text(text)

        self.parser.parse(state)

        blocks = state.blocks
        return blocks
        # parsed_blocks = self._parse_blocks(blocks)
        # return document.Document(parsed_blocks)


reader = MarkdownBlockReader()
# md = """
# # **Heading**

# This is a paragraph with *emph* and **strong**.

# Some code

#     print("Hello, World!")
#     do(smth)

# More code covered in block quote
# > ```python
# > print("Hello, World!")
# > do(smth)
# > ```
# > > One more level
# """

md = """
1. outer
    + he
    + low
2. outeer
"""
print(reader.parse(md))
