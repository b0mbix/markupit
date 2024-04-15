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

    def to_dict(self) -> dict:
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

    @abstractmethod
    def to_json(self) -> Any:
        """Convert the element to a JSON representation of AST.

        :return: The element as a JSON object.
        :rtype: Any
        """


class Inline(Element):
    pass


class Block(Element):
    pass


class MetaValue(Element):
    pass


class EnumElement(Element):
    pass


class ContentElement(Element):
    pass
