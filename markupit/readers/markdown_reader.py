from .markdown_block_reader import MarkdownBlockReader
from .reader import Reader
from ..structure.document import Document


class MarkdownReader(Reader):
    """A class representing a Markdown reader."""

    def __init__(self) -> None:
        self.block_reader = MarkdownBlockReader()
        super().__init__()

    def read(self, content: str) -> Document:
        """Read the content and return a Document.

        :param content: The content to read.
        :type content: str
        :return: The Document object.
        :rtype: Document
        """
        return self.block_reader.parse(content)
