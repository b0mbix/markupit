import re
import string

CONVERT_TAB_TO_SPACES_REGEX = re.compile(r"^( {0,3})\t", flags=re.M)
PUNCTUATION = rf"[{re.escape(string.punctuation)}]"
ESCAPE_CHAR_REGEX = re.compile(rf"\\({PUNCTUATION})")


def convert_leading_tabs_to_spaces(text: str, tab_width: int = 4) -> str:
    def replace_tabs_with_spaces(match: re.Match[str]) -> str:
        matched_string = match.group(1)
        return matched_string + " " * (tab_width - len(matched_string))

    return CONVERT_TAB_TO_SPACES_REGEX.sub(replace_tabs_with_spaces, text)


def convert_all_tabs_to_spaces(text: str, tab_width: int = 4) -> str:
    replacement = r"\1" + (" " * tab_width)
    return CONVERT_TAB_TO_SPACES_REGEX.sub(replacement, text)


def unescape_char(text: str) -> str:
    return ESCAPE_CHAR_REGEX.sub(r"\1", text)
