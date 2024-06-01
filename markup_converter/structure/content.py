from .enum import Alignment, CitationMode, ColWidth, ListNumberDelim, ListNumberStyle
from .general_types import Block, ContentElement, Inline


class Attr(ContentElement):
    """Class representing an Attr element.

    :param content: The content of the element.
    :type content: list
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 3,
                isinstance(content[0], str),
                isinstance(content[1], list),
                all(isinstance(i, str) for i in content[1]),
                isinstance(content[2], list),
                all(isinstance(i, list) for i in content[2]),
                all(len(i) == 2 for i in content[2]),
                all(isinstance(i[0], str) for i in content[2]),
                all(isinstance(i[1], str) for i in content[2]),
            ]
        ):
            raise TypeError("Content must be of a type [str, List[str], List[[str, str]]]")
        super().__init__(content=content)


class Format(ContentElement):
    """Class representing a Format element.

    :param content: The content of the element.
    :type content: str
    """

    def __init__(self, content: str) -> None:
        if not isinstance(content, str):
            raise TypeError("Content must be a string")
        super().__init__(content=content)


class Caption(ContentElement):
    """Class representing a Caption element.

    :param content: The content of the element.
    :type content: [List[Inline] | null, List[Block]]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 2,
                isinstance(content[0], list) or content[0] is None,
                all(isinstance(i, Block) for i in content[1]),
            ]
        ):
            raise TypeError("Content must be of a type [List[Inline] | null, List[Block]]")
        super().__init__(content=content)


class ColSpec(ContentElement):
    """Class representing a ColSpec element.

    :param content: The content of the element.
    :type content: [Alignment, ColWidth]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 2,
                isinstance(content[0], Alignment),
                isinstance(content[1], ColWidth),
            ]
        ):
            raise TypeError("Content must be of a type [Alignment, ColWidth]")
        super().__init__(content=content)


class TableHead(ContentElement):
    """Class representing a TableHead element.

    :param content: The content of the element.
    :type content: [Attr, List[Row]]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 2,
                isinstance(content[0], Attr),
                isinstance(content[1], list),
                all(isinstance(i, Row) for i in content[1]),
            ]
        ):
            raise TypeError("Content must be of a type [Attr, List[Row]]")
        super().__init__(content=content)


class TableBody(ContentElement):
    """Class representing a TableBody element.

    :param content: The content of the element.
    :type content: [Attr, int, List[Row], List[Row]]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 4,
                isinstance(content[0], Attr),
                isinstance(content[1], int),  # RowHeadColumns
                isinstance(content[2], list),
                all(isinstance(i, Row) for i in content[2]),
                isinstance(content[3], list),
                all(isinstance(i, Row) for i in content[3]),
            ]
        ):
            raise TypeError("Content must be of a type [Attr, int, List[Row], List[Row]]")
        super().__init__(content=content)


class TableFoot(ContentElement):
    """Class representing a TableFoot element.

    :param content: The content of the element.
    :type content: [Attr, List[Row]]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 2,
                isinstance(content[0], Attr),
                isinstance(content[1], list),
                all(isinstance(i, Row) for i in content[1]),
            ]
        ):
            raise TypeError("Content must be of a type [Attr, List[Row]]")
        super().__init__(content=content)


class ListAttributes(ContentElement):
    """Class representing a ListAttributes element.

    :param content: The content of the element.
    :type content: [int, ListNumberStyle, ListNumberDelim]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 3,
                isinstance(content[0], int),
                isinstance(content[1], ListNumberStyle),
                isinstance(content[2], ListNumberDelim),
            ]
        ):
            raise TypeError("Content must be of a type [int, ListNumberStyle, ListNumberDelim]")
        super().__init__(content=content)


class Target(ContentElement):
    """Class representing a Target element.

    :param content: The content of the element.
    :type content: [str, str]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 2,
                isinstance(content[0], str),  # URL
                isinstance(content[1], str),  # Title
            ]
        ):
            raise TypeError("Content must be of a type [str, str]")
        super().__init__(content=content)


class Citation(ContentElement):
    """Class representing a Citation element.

    :param content: The content of the element.
    :type content: [str, List[Inline], List[Inline], CitationMode, int, int]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 6,
                isinstance(content[0], str),  # CitationId
                isinstance(content[1], list),  # CitationPrefix
                all(isinstance(i, Inline) for i in content[1]),
                isinstance(content[2], list),  # CitationSuffix
                all(isinstance(i, Inline) for i in content[2]),
                isinstance(content[3], CitationMode),
                isinstance(content[4], int),  # CitationNoteNum
                isinstance(content[5], int),  # CitationHash
            ]
        ):
            raise TypeError("Content must be of a type [str, List[Inline], List[Inline], CitationMode, int, int]")
        super().__init__(content=content)


class Row(ContentElement):
    """Class representing a Row element.

    :param content: The content of the element.
    :type content: [Attr, List[Cell]]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 2,
                isinstance(content[0], Attr),
                isinstance(content[1], list),
                all(isinstance(i, Cell) for i in content[1]),
            ]
        ):
            raise TypeError("Content must be of a type [Attr, List[Cell]]")
        super().__init__(content=content)


class Cell(ContentElement):
    """Class representing a Cell element.

    :param content: The content of the element.
    :type content: [Attr, Alignment, int, int, List[Block]]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 5,
                isinstance(content[0], Attr),
                isinstance(content[1], Alignment),
                isinstance(content[2], int),  # RowSpan
                isinstance(content[3], int),  # ColSpan
                isinstance(content[4], list),
                all(isinstance(i, Block) for i in content[4]),
            ]
        ):
            raise TypeError("Content must be of a type [Attr, Alignment, int, int, List[Block]]")
        super().__init__(content=content)
