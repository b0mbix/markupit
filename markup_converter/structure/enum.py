from .general_types import EnumElement


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
