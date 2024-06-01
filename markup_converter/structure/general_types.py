from abc import ABC, abstractmethod
from typing import Any


class Element(ABC):
    """An abstract class representing an element in a document.

    :param tag: The name describing type of element.
    :type tag: str, optional
    :param content: The content of the element.
    :type content: Any, optional
    """

    def __init__(self, tag: str = None, content: Any = None) -> None:
        if tag is None:
            tag = self.__class__.__name__
        self.tag = tag
        self.content = content

    def __str__(self) -> str:
        return f"{self.tag}: {self.content}"

    def _element_to_json(self, el):
        """Helper method to convert element to JSON."""
        if any([isinstance(el, str), isinstance(el, int), isinstance(el, float)]):
            return el
        if isinstance(el, list):
            return [self._element_to_json(sub_el) for sub_el in el]
        return el.to_json()

    @abstractmethod
    def to_json(self) -> Any:
        """Convert the element to a JSON representation of AST.

        :return: The element as a JSON object.
        :rtype: Any
        """


class Inline(Element):
    """A class representing an element of Inline type.

    :param content: The content of the element.
    :type content: Any, optional
    """

    def __init__(self, content: Any = None) -> None:
        super().__init__(content=content)

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
        return {"t": self.tag, "c": [self._element_to_json(el) for el in self.content]}


class Block(Element):
    """A class representing an element of Block type.

    :param content: The content of the element.
    :type content: Any, optional
    """

    def __init__(self, content: Any = None) -> None:
        super().__init__(content=content)

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
        return {"t": self.tag, "c": [self._element_to_json(el) for el in self.content]}


class MetaValue(Element):
    pass


class ContentElement(Element):
    """Abstract class representing an element that is not represented by its tag in JSON.

    :param content: The content of the element.
    :type content: Any
    """

    def __init__(self, content: Any) -> None:
        super().__init__(content=content)

    def to_json(self) -> Any:
        if isinstance(self.content, str):
            return self.content
        if not isinstance(self.content, list):
            return self.content.content_to_json()
        return {"t": self.tag, "c": [self._element_to_json(el) for el in self.content]}


class EnumElement(Element):
    """Class representing an element of Enum type.

    :param content: Chosen value from the enumeration.
    :type content: str
    """

    def __init__(self, content: str) -> None:
        super().__init__(content=content)

    def to_json(self) -> str:
        return {"t": self.content}
