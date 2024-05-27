from .content import Attr, Citation, Target
from .enum import MathType, QuoteType
from .general_types import Block, Inline


class Space(Inline):
    """A class representing a Space element of Inline type."""

    def __init__(self) -> None:
        super().__init__()


class LineBreak(Inline):
    """A class representing a LineBreak element of Inline type."""

    def __init__(self) -> None:
        super().__init__()


class SoftBreak(Inline):
    """A class representing a SoftBreak element of Inline type."""

    def __init__(self) -> None:
        super().__init__()


class Str(Inline):
    """A class representing a Str element of Inline type.

    :param content: The content of the element.
    :type content: str
    """

    def __init__(self, content: str) -> None:
        if not isinstance(content, str):
            raise TypeError("Content must be a string")
        super().__init__(content=content)


class Emph(Inline):
    """A class representing an Emph element of Inline type.

    :param content: The content of the element.
    :type content: List[Inline]
    """

    def __init__(self, content: list) -> None:
        if not (isinstance(content, list) and all(isinstance(i, Inline) for i in content)):
            raise TypeError("Content must be of a type List[Inline]")
        super().__init__(content=content)


class Underline(Inline):
    """A class representing an Underline element of Inline type.

    :param content: The content of the element.
    :type content: List[Inline]
    """

    def __init__(self, content: list) -> None:
        if not (isinstance(content, list) and all(isinstance(i, Inline) for i in content)):
            raise TypeError("Content must be of a type List[Inline]")
        super().__init__(content=content)


class Strong(Inline):
    """A class representing a Strong element of Inline type.

    :param content: The content of the element.
    :type content: List[Inline]
    """

    def __init__(self, content: list) -> None:
        if not (isinstance(content, list) and all(isinstance(i, Inline) for i in content)):
            raise TypeError("Content must be of a type List[Inline]")
        super().__init__(content=content)


class Strikeout(Inline):
    """A class representing a Strikeout element of Inline type.

    :param content: The content of the element.
    :type content: List[Inline]
    """

    def __init__(self, content: list) -> None:
        if not (isinstance(content, list) and all(isinstance(i, Inline) for i in content)):
            raise TypeError("Content must be of a type List[Inline]")
        super().__init__(content=content)


class Superscript(Inline):
    """A class representing a Superscript element of Inline type.

    :param content: The content of the element.
    :type content: List[Inline]
    """

    def __init__(self, content: list) -> None:
        if not (isinstance(content, list) and all(isinstance(i, Inline) for i in content)):
            raise TypeError("Content must be of a type List[Inline]")
        super().__init__(content=content)


class Subscript(Inline):
    """A class representing a Subscript element of Inline type.

    :param content: The content of the element.
    :type content: List[Inline]
    """

    def __init__(self, content: list) -> None:
        if not (isinstance(content, list) and all(isinstance(i, Inline) for i in content)):
            raise TypeError("Content must be of a type List[Inline]")
        super().__init__(content=content)


class SmallCaps(Inline):
    """A class representing a SmallCaps element of Inline type.

    :param content: The content of the element.
    :type content: List[Inline]
    """

    def __init__(self, content: list) -> None:
        if not (isinstance(content, list) and all(isinstance(i, Inline) for i in content)):
            raise TypeError("Content must be of a type List[Inline]")
        super().__init__(content=content)


class Note(Inline):
    """A class representing a Note element of Inline type.

    :param content: The content of the element.
    :type content: List[Block]
    """

    def __init__(self, content: list) -> None:
        if not (isinstance(content, list) and all(isinstance(i, Block) for i in content)):
            raise TypeError("Content must be of a type List[Block]")
        super().__init__(content=content)


class Span(Inline):
    """A class representing a Span element of Inline type.

    :param content: The content of the element.
    :type content: [Attr, List[Inline]]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 2,
                isinstance(content[0], Attr),
                all(isinstance(i, Inline) for i in content[1]),
            ]
        ):
            raise TypeError("Content must be of a type [Attr, List[Inline]]")
        super().__init__(content=content)


class Quoted(Inline):
    """A class representing a Quoted element of Inline type.

    :param content: The content of the element.
    :type content: [QuoteType, List[Inline]]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 2,
                isinstance(content[0], QuoteType),
                all(isinstance(i, Inline) for i in content[1]),
            ]
        ):
            raise TypeError("Content must be of a type [QuoteType, List[Inline]]")
        super().__init__(content=content)


class Cite(Inline):
    """A class representing a Cite element of Inline type.

    :param content: The content of the element.
    :type content: [List[Citation], List[Inline]]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 2,
                all(isinstance(i, Citation) for i in content[0]),
                all(isinstance(i, Inline) for i in content[1]),
            ]
        ):
            raise TypeError("Content must be of a type [List[Citation], List[Inline]]")
        super().__init__(content=content)


class Link(Inline):
    """A class representing a Link element of Inline type.

    :param content: The content of the element.
    :type content: [Attr, List[Inline], Target]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 3,
                isinstance(content[0], Attr),
                all(isinstance(i, Inline) for i in content[1]),
                isinstance(content[2], Target),
            ]
        ):
            raise TypeError("Content must be of a type [Attr, List[Inline], Target]")
        super().__init__(content=content)


class Image(Inline):
    """A class representing an Image element of Inline type.

    :param content: The content of the element.
    :type content: [Attr, List[Inline], Target]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 3,
                isinstance(content[0], Attr),
                all(isinstance(i, Inline) for i in content[1]),
                isinstance(content[2], Target),
            ]
        ):
            raise TypeError("Content must be of a type [Attr, List[Inline], Target]")
        super().__init__(content=content)


class Code(Inline):
    """A class representing a Code element of Inline type.

    :param content: The content of the element.
    :type content: [Attr, str]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 2,
                isinstance(content[0], Attr),
                isinstance(content[1], str),
            ]
        ):
            raise TypeError("Content must be of a type [Attr, str]")
        super().__init__(content=content)


class Math(Inline):
    """A class representing a Math element of Inline type.

    :param content: The content of the element.
    :type content: [EnumElement, str]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 2,
                isinstance(content[0], MathType),
                isinstance(content[1], str),
            ]
        ):
            raise TypeError("Content must be of a type [MathType, str]")
        super().__init__(content=content)


class RawInline(Inline):
    """A class representing a RawInline element of Inline type.

    :param content: The content of the element.
    :type content: [Format, str]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 2,
                isinstance(content[0], str),
                isinstance(content[1], str),
            ]
        ):
            raise TypeError("Content must be of a type [Format, str]")
        super().__init__(content=content)
