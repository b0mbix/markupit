from enum import Enum

from . import readers, writers


class SupportedFrom(str, Enum):
    markdown = "md"


reader_classes = {SupportedFrom.markdown: readers.MarkdownReader}


class SupportedTo(str, Enum):
    json = "json"
    typst = "typst"


writer_classes = {SupportedTo.json: writers.JsonWriter, SupportedTo.typst: writers.TypstWriter}
