from typing import List

from .general_types import Element


class Document:
    """A class representing a document. It contains a list of blocks.

    :param blocks: A list of blocks in the document.
    :type blocks: List[Element], optional
    """

    def __init__(self, blocks: List["Element"] = None) -> None:
        if blocks is None:
            blocks = []
        if not (isinstance(blocks, list) and all(isinstance(i, Element) for i in blocks)):
            raise TypeError("Blocks must be of a type List[Element] or None")
        self.blocks = blocks

    def __str__(self) -> str:
        return f"Blocks: {self.blocks}"

    def add_block(self, block: "Element") -> None:
        """Add a block to the end of the document.

        :param block: The block to add.
        :type block: Element
        """
        if not isinstance(block, Element):
            raise TypeError("Block must be of a type Element")
        self.blocks.append(block)

    def add_blocks(self, blocks: List["Element"]) -> None:
        """Add a list of blocks to the end of the document.

        :param blocks: The blocks to add.
        :type blocks: List[Element]
        """
        if not (isinstance(blocks, list) and all(isinstance(i, Element) for i in blocks)):
            raise TypeError("Blocks must be of a type List[Element]")
        self.blocks.extend(blocks)

    def to_json(self) -> dict:
        """Convert the document to a dictionary representing AST.

        :return: The document as a dictionary.
        :rtype: dict
        """
        return {"blocks": [block.to_json() for block in self.blocks]}
