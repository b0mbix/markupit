from typing import Any

from .general_types import ContentElement, Element, EnumElement


class Inline(Element):
    """A class representing an element of Inline type.

    :param tag: The name describing type of element.
    :type tag: str
    :param content: The content of the element.
    :type content: Any, optional
    """

    def __init__(self, tag: str, content: Any = None) -> None:
        if tag in ("Space", "SoftBreak", "LineBreak"):
            if content is not None:
                raise ValueError(f"Content must be None for {tag}")
        elif tag == "Str":
            if not isinstance(content, str):
                raise ValueError(f"Content must be a string for {tag}")
        elif tag in ("Emph", "Underline", "Strong", "Strikeout", "Superscript", "Subscript", "SmallCaps"):
            if not (isinstance(content, list) and all(isinstance(i, Inline) for i in content)):
                raise ValueError(f"Content must be of a type List[Inline] for {tag}")
        elif tag == "Note":
            if not (isinstance(content, list) and all(isinstance(i, Block) for i in content)):
                raise ValueError(f"Content must be of a type List[Block] for {tag}")
        elif tag == "Span":
            if not all(
                [
                    isinstance(content, list),
                    len(content) == 2,
                    isinstance(content[0], Attr),
                    all(isinstance(i, Inline) for i in content[1]),
                ]
            ):
                raise ValueError(f"Content must be of a type [Attr, List[Inline]] for {tag}")
        elif tag == "Quoted":
            if not all(
                [
                    isinstance(content, list),
                    len(content) == 2,
                    isinstance(content[0], QuoteType),
                    all(isinstance(i, Inline) for i in content[1]),
                ]
            ):
                raise ValueError(f"Content must be of a type [QuoteType, List[Inline]] for {tag}")
        elif tag == "Cite":
            if not all(
                [
                    isinstance(content, list),
                    len(content) == 2,
                    all(isinstance(i, Citation) for i in content[0]),
                    all(isinstance(i, Inline) for i in content[1]),
                ]
            ):
                raise ValueError(f"Content must be of a type [List[Citation], List[Inline]] for {tag}")
        elif tag in ("Link", "Image"):
            if not all(
                [
                    isinstance(content, list),
                    len(content) == 3,
                    isinstance(content[0], Attr),
                    all(isinstance(i, Inline) for i in content[1]),
                    isinstance(content[2], Target),
                ]
            ):
                raise ValueError(f"Content must be of a type [Attr, List[Inline], Target] for {tag}")
        elif tag == "Code":
            if not all(
                [
                    isinstance(content, list),
                    len(content) == 2,
                    isinstance(content[0], Attr),
                    isinstance(content[1], str),
                ]
            ):
                raise ValueError(f"Content must be of a type [Attr, str] for {tag}")
        elif tag == "Math":
            if not all(
                [
                    isinstance(content, list),
                    len(content) == 2,
                    isinstance(content[0], EnumElement),
                    isinstance(content[1], str),
                ]
            ):
                raise ValueError(f"Content must be of a type [MathType, str] for {tag}")
        elif tag == "RawInline":
            if not all(
                [
                    isinstance(content, list),
                    len(content) == 2,
                    isinstance(content[0], Format),
                    isinstance(content[1], str),
                ]
            ):
                raise ValueError(f"Content must be of a type [Format, str] for {tag}")
        else:
            raise ValueError(f"Unknown tag: {tag}")
        super().__init__(tag, content)

    def to_json(self) -> dict:
        """Convert the element to a JSON representation of AST.

        :return: The element as a JSON object.
        :rtype: dict
        """
        if self.content is None:
            return {"t": self.tag}
        if isinstance(self.content, str):
            return {"t": self.tag, "c": self.content}
        if not isinstance(self.content, list):
            return {"t": self.tag, "c": self.content.content_to_json()}
        return {"t": self.tag, "c": [el if isinstance(el, str) else el.to_json() for el in self.content]}


class Block(Element):
    """A class representing an element of Block type.

    :param tag: The name describing type of element.
    :type tag: str
    :param content: The content of the element.
    :type content: Any, optional
    """

    def __init__(self, tag: str, content: Any = None) -> None:
        if tag in ("Null", "HorizontalRule"):
            if content is not None:
                raise ValueError(f"Content must be None for {tag}")
        elif tag in ("Plain", "Para"):
            if not (isinstance(content, list) and all(isinstance(i, Inline) for i in content)):
                raise ValueError(f"Content must be of a type List[Inline] for {tag}")
        elif tag == "BlockQuote":
            if not (isinstance(content, list) and all(isinstance(i, Block) for i in content)):
                raise ValueError(f"Content must be of a type List[Block] for {tag}")
        elif tag == "CodeBlock":
            if not all(
                [
                    isinstance(content, list),
                    len(content) == 2,
                    isinstance(content[0], Attr),
                    isinstance(content[1], str),
                ]
            ):
                raise ValueError(f"Content must be of a type [Attr, str] for {tag}")
        elif tag == "RawBlock":
            if not all(
                [
                    isinstance(content, list),
                    len(content) == 2,
                    isinstance(content[0], Format),
                    isinstance(content[1], str),
                ]
            ):
                raise ValueError(f"Content must be of a type [Format, str] for {tag}")
        elif tag == "Div":
            if not all(
                [
                    isinstance(content, list),
                    len(content) == 2,
                    isinstance(content[0], Attr),
                    isinstance(content[1], list),
                    all(isinstance(i, Block) for i in content[1]),
                ]
            ):
                raise ValueError(f"Content must be of a type [Attr, List[Block]] for {tag}")
        elif tag == "Header":
            if not all(
                [
                    isinstance(content, list),
                    len(content) == 3,
                    isinstance(content[0], int),
                    isinstance(content[1], Attr),
                    isinstance(content[2], list),
                    all(isinstance(i, Inline) for i in content[1]),
                ]
            ):
                raise ValueError(f"Content must be of a type [int, Attr, List[Inline]] for {tag}")
        elif tag == "Figure":
            if not all(
                [
                    isinstance(content, list),
                    len(content) == 3,
                    isinstance(content[0], Attr),
                    isinstance(content[1], Caption),
                    isinstance(content[2], list),
                    all(isinstance(i, Block) for i in content[2]),
                ]
            ):
                raise ValueError(f"Content must be of a type [Attr, Caption, List[Block]] for {tag}")
        elif tag == "Table":
            if not all(
                [
                    isinstance(content, list),
                    len(content) == 6,
                    isinstance(content[0], Attr),
                    isinstance(content[1], Caption),
                    isinstance(content[2], list),
                    all(isinstance(i, ColSpec) for i in content[2]),
                    isinstance(content[3], TableHead),
                    isinstance(content[4], list),
                    all(isinstance(i, TableBody) for i in content[4]),
                    isinstance(content[5], TableFoot),
                ]
            ):
                raise ValueError(
                    f"Content must be of a type [Attr, Caption, List[ColSpec],"
                    f"TableHead, List[TableBody], TableFoot] for {tag}"
                )
        elif tag == "BulletList":
            if not all(
                [
                    isinstance(content, list),
                    all(isinstance(i, list) for i in content),
                    all(all(isinstance(j, Block) for j in i) for i in content),
                ]
            ):
                raise ValueError(f"Content must be of a type List[List[Block]] for {tag}")
        elif tag == "LineBlock":
            if not all(
                [
                    isinstance(content, list),
                    all(isinstance(i, list) for i in content),
                    all(all(isinstance(j, Inline) for j in i) for i in content),
                ]
            ):
                raise ValueError(f"Content must be of a type List[List[Inline]] for {tag}")
        elif tag == "OrderedList":
            if not all(
                [
                    isinstance(content, list),
                    len(content) == 2,
                    isinstance(content[0], ListAttributes),
                    isinstance(content[1], list),
                    all(isinstance(i, list) for i in content[1]),
                    all(all(isinstance(j, Block) for j in i) for i in content[1]),
                ]
            ):
                raise ValueError(f"Content must be of a type [ListAttributes, List[List[Block]]] for {tag}")
        elif tag == "DefinitionList":
            if not all(
                [
                    isinstance(content, list),
                    all(isinstance(i, list) for i in content),
                    all(len(i) == 2 for i in content),
                    all(isinstance(i[0], list) for i in content),
                    all(all(isinstance(j, Inline) for j in i[0]) for i in content),
                    all(isinstance(i[1], list) for i in content),
                    all(all(isinstance(j, list) for j in i[1]) for i in content),
                    all(all(all(isinstance(k, Block) for k in j) for j in i[1]) for i in content),
                ]
            ):
                raise ValueError(
                    f"Content must be of a type List[List[List[Inline]]," f"List[List[List[Block]]]] for {tag}"
                )
        else:
            raise ValueError(f"Unknown tag: {tag}")
        super().__init__(tag, content)

    def to_json(self) -> dict:
        """Convert the element to a JSON representation of AST.

        :return: The element as a JSON object.
        :rtype: dict
        """
        if self.content is None:
            return {"t": self.tag}
        if isinstance(self.content, str):
            return {"t": self.tag, "c": self.content}
        if not isinstance(self.content, list):
            return {"t": self.tag, "c": self.content.content_to_json()}
        return {"t": self.tag, "c": [el if isinstance(el, str) else el.to_json() for el in self.content]}


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
                all(len(content[2][i]) == 2 for i in content[2]),
                all(isinstance(i[0], str) for i in content[2]),
                all(isinstance(i[1], str) for i in content[2]),
            ]
        ):
            raise ValueError("Content must be of a type [str, List[str], List[[str, str]]]")
        super().__init__(content=content)


class Format(ContentElement):
    """Class representing a Format element.

    :param content: The content of the element.
    :type content: str
    """

    def __init__(self, content: str) -> None:
        if not isinstance(content, str):
            raise ValueError("Content must be a string")
        super().__init__(content=content)


class Caption(ContentElement):
    """Class representing a Caption element.

    :param content: The content of the element.
    :type content: list
    """

    def __init__(self, content: Any) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 2,
                isinstance(content[0], list) or content[0] is None,
                all(isinstance(i, Block) for i in content[1]),
            ]
        ):
            raise ValueError("Content must be of a type [List[Inline] | null, List[Block]]")
        super().__init__(content=content)


class ColSpec(ContentElement):
    """Class representing a ColSpec element.

    :param content: The content of the element.
    :type content: list
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
            raise ValueError("Content must be of a type [Alignment, ColWidth]")
        super().__init__(content=content)


class TableHead(ContentElement):
    """Class representing a TableHead element.

    :param content: The content of the element.
    :type content: list
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
            raise ValueError("Content must be of a type [Attr, List[Row]]")
        super().__init__(content=content)


class TableBody(ContentElement):
    """Class representing a TableBody element.

    :param content: The content of the element.
    :type content: list
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
            raise ValueError("Content must be of a type [Attr, int, List[Row], List[Row]]")
        super().__init__(content=content)


class TableFoot(ContentElement):
    """Class representing a TableFoot element.

    :param content: The content of the element.
    :type content: list
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
            raise ValueError("Content must be of a type [Attr, List[Row]]")
        super().__init__(content=content)


class ListAttributes(ContentElement):
    """Class representing a ListAttributes element.

    :param content: The content of the element.
    :type content: list
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
            raise ValueError("Content must be of a type [int, ListNumberStyle, ListNumberDelim]")
        super().__init__(content=content)


class Target(ContentElement):
    """Class representing a Target element.

    :param content: The content of the element.
    :type content: list
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
            raise ValueError("Content must be of a type [str, str]")
        super().__init__(content=content)


class Citation(ContentElement):
    """Class representing a Citation element.

    :param content: The content of the element.
    :type content: list
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
            raise ValueError("Content must be of a type [str, List[Inline], List[Inline], CitationMode, int, int]")
        super().__init__(content=content)


class Row(ContentElement):
    """Class representing a Row element.

    :param content: The content of the element.
    :type content: list
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
            raise ValueError("Content must be of a type [Attr, List[Cell]]")
        super().__init__(content=content)


class Cell(ContentElement):
    """Class representing a Cell element.

    :param content: The content of the element.
    :type content: list
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
            raise ValueError("Content must be of a type [Attr, Alignment, int, int, List[Block]]")
        super().__init__(content=content)


class MathType(EnumElement):
    """Class representing a MathType enum element.

    :param content: Chosen value from the enumeration.
    :type content: str
    """

    def __init__(self, content: str) -> None:
        if content not in ("DisplayMath", "InlineMath"):
            raise ValueError("Content must be one of 'DisplayMath', 'InlineMath'")
        super().__init__(content=content)


class Alignment(EnumElement):
    """Class representing an Alignment enum element.

    :param content: Chosen value from the enumeration.
    :type content: str
    """

    def __init__(self, content: str) -> None:
        if content not in ("AlignLeft", "AlignCenter", "AlignRight", "AlignDefault"):
            raise ValueError("Content must be one of 'AlignLeft', 'AlignCenter', 'AlignRight', 'AlignDefault'")
        super().__init__(content=content)


class ListNumberStyle(EnumElement):
    """Class representing a ListNumberStyle enum element.

    :param content: Chosen value from the enumeration.
    :type content: str
    """

    def __init__(self, content: str) -> None:
        if content not in (
            "DefaultStyle",
            "Example",
            "Decimal",
            "LowerRoman",
            "UpperRoman",
            "LowerAlpha",
            "UpperAlpha",
        ):
            raise ValueError(
                "Content must be one of 'DefaultStyle', 'Example', 'Decimal',",
                "'LowerRoman', 'UpperRoman', 'LowerAlpha', 'UpperAlpha'",
            )
        super().__init__(content=content)


class ListNumberDelim(EnumElement):
    """Class representing a ListNumberDelim enum element.

    :param content: Chosen value from the enumeration.
    :type content: str
    """

    def __init__(self, content: str) -> None:
        if content not in ("DefaultDelim", "Period", "OneParen", "TwoParens"):
            raise ValueError("Content must be one of 'DefaultDelim', 'Period', 'OneParen', 'TwoParens'")
        super().__init__(content=content)


class CitationMode(EnumElement):
    """Class representing a CitationMode enum element.

    :param content: Chosen value from the enumeration.
    :type content: str
    """

    def __init__(self, content: str) -> None:
        if content not in ("AuthorInText", "SuppressAuthor", "NormalCitation"):
            raise ValueError("Content must be one of 'AuthorInText', 'SuppressAuthor', 'NormalCitation'")
        super().__init__(content=content)


class QuoteType(EnumElement):
    """Class representing a QuoteType enum element.

    :param content: Chosen value from the enumeration.
    :type content: str
    """

    def __init__(self, content: str) -> None:
        if content not in ("SingleQuote", "DoubleQuote"):
            raise ValueError("Content must be one of 'SingleQuote', 'DoubleQuote'")
        super().__init__(content=content)


class ColWidth(EnumElement):
    """Class representing a ColWidth enum element.

    :param content: Chosen value from the enumeration.
    :type content: str
    :param width: The width of the column, used when content is 'ColWidth'.
    :type width: float, optional
    """

    def __init__(self, content: str, width: float = None) -> None:
        if content not in ("ColWidthDefault", "ColWidth"):
            raise ValueError("Content must be one of 'ColWidthDefault', 'ColWidth'")
        if content == "ColWidth" and not isinstance(width, float):
            raise ValueError("Width must be a float when content is 'ColWidth'")
        self.width = width
        super().__init__(content=content)
