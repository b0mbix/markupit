from abc import ABC, abstractmethod

from .. import structure as st
from ..structure.document import Document
from ..structure.general_types import Element


class Writer(ABC):
    """An abstract class representing a writer.

    :param input: The document to convert.
    :type input: structure.Document
    """

    def __init__(self, input: Document) -> None:
        self.doc = input
        self.convert_actions = {
            st.Inline.Space: self.convert_space,
            st.Inline.SoftBreak: self.convert_soft_break,
            st.Inline.LineBreak: self.convert_line_break,
            st.Inline.Str: self.convert_str,
            st.Inline.Emph: self.convert_emph,
            st.Inline.Underline: self.convert_underline,
            st.Inline.Strong: self.convert_strong,
            st.Inline.Strikeout: self.convert_strikeout,
            st.Inline.Superscript: self.convert_superscript,
            st.Inline.Subscript: self.convert_subscript,
            st.Inline.SmallCaps: self.convert_small_caps,
            st.Inline.Note: self.convert_note,
            st.Inline.Link: self.convert_link,
            st.Inline.Image: self.convert_image,
            st.Inline.Code: self.convert_code,
            st.Inline.RawInline: self.convert_raw_inline,
            st.Block.HorizontalRule: self.convert_horizontal_rule,
            st.Block.Plain: self.convert_plain,
            st.Block.Para: self.convert_para,
            st.Block.BlockQuote: self.convert_block_quote,
            st.Block.CodeBlock: self.convert_code_block,
            st.Block.RawBlock: self.convert_raw_block,
            st.Block.Header: self.convert_header,
            st.Block.Table: self.convert_table,
            st.Block.BulletList: self.convert_bullet_list,
            st.Block.OrderedList: self.convert_ordered_list,
        }

    def write(self) -> str:
        """Convert the document to a text format according to writer.

        :return: The converted document.
        """
        result = ""
        for block in self.doc.blocks:
            result += self.convert_element(block)
        return result

    def write_file(self, path: str) -> None:
        """Convert and write the document to a file at the given path.

        :param path: The path to write the document to.
        :type path: str
        """
        with open(path, "w") as f:
            f.write(self.write())

    def convert_element(self, obj: Element) -> str:
        """Find and perform conversion for the given element.

        :param obj: The element to convert.
        :type obj: Element
        :return: The converted element.
        """
        if isinstance(obj, list):
            return "".join([self.convert_element(el) for el in obj])
        if type(obj) not in self.convert_actions:
            raise NotImplementedError(f"No converter implemented for {type(obj)}")
        return self.convert_actions[type(obj)](obj)

    @abstractmethod
    def convert_space(self, obj: st.Inline.Space) -> str:
        pass

    @abstractmethod
    def convert_soft_break(self, obj: st.Inline.SoftBreak) -> str:
        pass

    @abstractmethod
    def convert_line_break(self, obj: st.Inline.LineBreak) -> str:
        pass

    @abstractmethod
    def convert_str(self, obj: st.Inline.Str) -> str:
        pass

    @abstractmethod
    def convert_emph(self, obj: st.Inline.Emph) -> str:
        pass

    @abstractmethod
    def convert_underline(self, obj: st.Inline.Underline) -> str:
        pass

    @abstractmethod
    def convert_strong(self, obj: st.Inline.Strong) -> str:
        pass

    @abstractmethod
    def convert_strikeout(self, obj: st.Inline.Strikeout) -> str:
        pass

    @abstractmethod
    def convert_superscript(self, obj: st.Inline.Superscript) -> str:
        pass

    @abstractmethod
    def convert_subscript(self, obj: st.Inline.Subscript) -> str:
        pass

    @abstractmethod
    def convert_small_caps(self, obj: st.Inline.SmallCaps) -> str:
        pass

    @abstractmethod
    def convert_note(self, obj: st.Inline.Note) -> str:
        pass

    @abstractmethod
    def convert_link(self, obj: st.Inline.Link) -> str:
        pass

    @abstractmethod
    def convert_image(self, obj: st.Inline.Image) -> str:
        pass

    @abstractmethod
    def convert_code(self, obj: st.Inline.Code) -> str:
        pass

    @abstractmethod
    def convert_raw_inline(self, obj: st.Inline.RawInline) -> str:
        pass

    @abstractmethod
    def convert_horizontal_rule(self, obj: st.Block.HorizontalRule) -> str:
        pass

    @abstractmethod
    def convert_plain(self, obj: st.Block.Plain) -> str:
        pass

    @abstractmethod
    def convert_para(self, obj: st.Block.Para) -> str:
        pass

    @abstractmethod
    def convert_block_quote(self, obj: st.Block.BlockQuote) -> str:
        pass

    @abstractmethod
    def convert_code_block(self, obj: st.Block.CodeBlock) -> str:
        pass

    @abstractmethod
    def convert_raw_block(self, obj: st.Block.RawBlock) -> str:
        pass

    @abstractmethod
    def convert_header(self, obj: st.Block.Header) -> str:
        pass

    @abstractmethod
    def convert_table(self, obj: st.Block.Table) -> str:
        pass

    @abstractmethod
    def convert_bullet_list(self, obj: st.Block.BulletList) -> str:
        pass

    @abstractmethod
    def convert_ordered_list(self, obj: st.Block.OrderedList) -> str:
        pass
