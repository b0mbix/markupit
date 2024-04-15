from typing import Any, List
from abc import ABC, abstractmethod


class Document:
    """A class representing a document. It contains a list of blocks.

    :param blocks: A list of blocks in the document.
    :type blocks: List[Element], optional
    """

    def __init__(self, blocks: List["Element"] = None) -> None:
        if blocks is None:
            blocks = []
        self.blocks = blocks

    def __str__(self) -> str:
        return f"Blocks: {self.blocks}"

    def add_block(self, block: "Element") -> None:
        """Add a block to the end of the document.

        :param block: The block to add.
        :type block: Element
        """
        self.blocks.append(block)

    def add_blocks(self, blocks: List["Element"]) -> None:
        """Add a list of blocks to the end of the document.

        :param blocks: The blocks to add.
        :type blocks: List[Element]
        """
        self.blocks.extend(blocks)

    def to_json(self) -> dict:
        """Convert the document to a dictionary representing AST.

        :return: The document as a dictionary.
        :rtype: dict
        """
        return {"blocks": [block.to_json() for block in self.blocks]}


class Element(ABC):
    """An abstract class representing an element in a document.

    :param tag: The name describing type of element.
    :type tag: str
    :param content: The content of the element.
    :type content: Any, optional
    :param attributes: A list of attributes of the element.
    """

    def __init__(self, tag: str, content: Any = None, attributes: list = None) -> None:
        self.tag = tag
        self.content = content
        self.attributes = attributes

    def __str__(self) -> str:
        return f"{self.tag}: {self.content}"

    def content_to_json(self) -> Any:
        """Convert the content of an element to a JSON representation of AST.

        :return: The content as a JSON object.
        :rtype: Any
        """
        if self.content is None:
            return None
        if isinstance(self.content, any(str, int, float)):
            return self.content
        if not isinstance(self.content, list):
            return self.content.content_to_json()
        return [el.to_json() for el in self.content]

    @abstractmethod
    def to_json(self) -> Any:
        """Convert the element to a JSON representation of AST.

        :return: The element as a JSON object.
        :rtype: Any
        """


class Inline(Element):
    """A class representing an element of Inline type in a document.

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
                    isinstance(content[0], EnumElement),
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

    def to_json(self) -> Any:
        if self.content is None:
            return {"t": self.tag}
        if isinstance(self.content, str):
            return {"t": self.tag, "c": self.content}
        if not isinstance(self.content, list):
            return {"t": self.tag, "c": self.content.content_to_json()}
        return {"t": self.tag, "c": [el.to_json() for el in self.content]}


class Block(Element):
    pass


class MetaValue(Element):
    pass


class EnumElement(Element):
    pass


class ContentElement(Element):
    pass


class Attr(ContentElement):
    pass


class Target(ContentElement):
    pass


class Format(ContentElement):
    pass


class Citation(ContentElement):
    pass


class MathType(EnumElement):
    pass
