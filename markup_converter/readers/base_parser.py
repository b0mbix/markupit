import re

from markup_converter.readers.state import BlockState


class BaseParser:
    """
    Base class for all parsers. It defines the basic interface for all parsers.
    """

    GRAMMAR_RULES = {}
    RULES_NAMES = []

    def __init__(self) -> None:
        self.grammar_rules = self.GRAMMAR_RULES.copy()
        self.rules = self.RULES_NAMES.copy()
        self._methods = {}
        self._compiled_regexs = {}
        self.sc_flag = re.MULTILINE

    def compile_regex(self, rules: list[str] = None) -> re.Pattern[str]:
        if rules is None:
            key = "$"
            rules = self.rules
        else:
            key = "|".join(rules)

        compiled_regex = self._compiled_regexs.get(key)
        if compiled_regex:
            return compiled_regex

        regex = "|".join(f"(?P<{k}>{self.grammar_rules[k]})" for k in rules)
        compiled_regex = re.compile(regex, self.sc_flag)
        self._compiled_regexs[key] = compiled_regex
        return compiled_regex

    @staticmethod
    def insert_rule(rules: list[str], name: str, before: str = None) -> None:
        if before and before in rules:
            index = rules.index(before)
            rules.insert(index, name)
        else:
            rules.append(name)

    def get_parse_method(self, m: re.Match[str], state: BlockState) -> int:
        lastgroup = m.lastgroup
        func = self._methods[lastgroup]
        return func(m, state)
