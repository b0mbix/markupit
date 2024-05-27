from .content import Attr, Caption, ColSpec, Format, ListAttributes, TableBody, TableFoot, TableHead
from .general_types import Block, Inline


class Null(Block):
    """A class representing a Null element of Block type."""

    def __init__(self) -> None:
        super().__init__()


class HorizontalRule(Block):
    """A class representing a HorizontalRule element of Block type."""

    def __init__(self) -> None:
        super().__init__()


class Plain(Block):
    """A class representing a Plain element of Block type.

    :param content: The content of the element.
    :type content: List[Inline]
    """

    def __init__(self, content: list) -> None:
        if not (isinstance(content, list) and all(isinstance(i, Inline) for i in content)):
            raise ValueError("Content must be of a type List[Inline]")
        super().__init__(content=content)


class Para(Block):
    """A class representing a Para element of Block type.

    :param content: The content of the element.
    :type content: List[Inline]
    """

    def __init__(self, content: list) -> None:
        if not (isinstance(content, list) and all(isinstance(i, Inline) for i in content)):
            raise ValueError("Content must be of a type List[Inline]")
        super().__init__(content=content)


class BlockQuote(Block):
    """A class representing a BlockQuote element of Block type.

    :param content: The content of the element.
    :type content: List[Block]
    """

    def __init__(self, content: list) -> None:
        if not (isinstance(content, list) and all(isinstance(i, Block) for i in content)):
            raise ValueError("Content must be of a type List[Block]")
        super().__init__(content=content)


class CodeBlock(Block):
    """A class representing a CodeBlock element of Block type.

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
            raise ValueError("Content must be of a type [Attr, str]")
        super().__init__(content=content)


class RawBlock(Block):
    """A class representing a RawBlock element of Block type.

    :param content: The content of the element.
    :type content: [Format, str]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 2,
                isinstance(content[0], Format),
                isinstance(content[1], str),
            ]
        ):
            raise ValueError("Content must be of a type [Format, str]")
        super().__init__(content=content)


class Div(Block):
    """A class representing a Div element of Block type.

    :param content: The content of the element.
    :type content: [Attr, List[Block]]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                len(content) == 2,
                isinstance(content[0], Attr),
                isinstance(content[1], list),
                all(isinstance(i, Block) for i in content[1]),
            ]
        ):
            raise ValueError("Content must be of a type [Attr, List[Block]]")
        super().__init__(content=content)


class Header(Block):
    """A class representing a Header element of Block type.

    :param content: The content of the element.
    :type content: [int, Attr, List[Inline]]
    """

    def __init__(self, content: list) -> None:
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
            raise ValueError("Content must be of a type [int, Attr, List[Inline]]")
        super().__init__(content=content)


class Figure(Block):
    """A class representing a Figure element of Block type.

    :param content: The content of the element.
    :type content: [Attr, Caption, List[Block]]
    """

    def __init__(self, content: list) -> None:
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
            raise ValueError("Content must be of a type [Attr, Caption, List[Block]]")
        super().__init__(content=content)


class Table(Block):
    """A class representing a Table element of Block type.

    :param content: The content of the element.
    :type content: [Attr, Caption, List[ColSpec], TableHead, List[TableBody], TableFoot]
    """

    def __init__(self, content: list) -> None:
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
                "Content must be of a type [Attr, Caption, List[ColSpec]," "TableHead, List[TableBody], TableFoot]"
            )
        super().__init__(content=content)


class BulletList(Block):
    """A class representing a BulletList element of Block type.

    :param content: The content of the element.
    :type content: List[List[Block]]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                all(isinstance(i, list) for i in content),
                all(all(isinstance(j, Block) for j in i) for i in content),
            ]
        ):
            raise ValueError("Content must be of a type List[List[Block]]")
        super().__init__(content=content)


class LineBlock(Block):
    """A class representing a LineBlock element of Block type.

    :param content: The content of the element.
    :type content: List[List[Inline]]
    """

    def __init__(self, content: list) -> None:
        if not all(
            [
                isinstance(content, list),
                all(isinstance(i, list) for i in content),
                all(all(isinstance(j, Inline) for j in i) for i in content),
            ]
        ):
            raise ValueError("Content must be of a type List[List[Inline]]")
        super().__init__(content=content)


class OrderedList(Block):
    """A class representing a OrderedList element of Block type.

    :param content: The content of the element.
    :type content: [ListAttributes, List[List[Block]]]
    """

    def __init__(self, content: list) -> None:
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
            raise ValueError("Content must be of a type [ListAttributes, List[List[Block]]]")
        super().__init__(content=content)


class DefinitionList(Block):
    """A class representing a DefinitionList element of Block type.

    :param content: The content of the element.
    :type content: List[List[List[Inline]], List[List[List[Block]]]]
    """

    def __init__(self, content: list) -> None:
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
            raise ValueError("Content must be of a type List[List[List[Inline]], List[List[List[Block]]]]")
        super().__init__(content=content)
