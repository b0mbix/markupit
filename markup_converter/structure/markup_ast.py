from typing import Any

from .content import Attr, Caption, Citation, ColSpec, Format, ListAttributes, TableBody, TableFoot, TableHead, Target
from .enum import QuoteType
from .general_types import Element, EnumElement


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
