from abc import ABC, abstractmethod
from ..structure.document import Document


class Reader(ABC):
    """An abstract class representing a reader."""

    def __init__(self) -> None:
        pass

    @abstractmethod
    def read(self, content: str) -> Document:
        """Read the content and return a Document.

        :param content: The content to read.
        :type content: str
        :return: The Document object.
        :rtype: Document
        """
        pass

    def read_file(self, path: str) -> Document:
        """Read the content of a file and return a Document.

        :param path: The path to the file.
        :type path: str
        :return: The Document object.
        :rtype: Document
        """
        with open(path, "r") as file:
            return self.read(file.read())
