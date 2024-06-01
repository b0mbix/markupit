from enum import Enum

from . import readers, writers


class SupportedFrom(str, Enum):
    markdown = "md"


reader_classes = {SupportedFrom.markdown: readers.MarkdownReader}


class SupportedTo(str, Enum):
    json = "json"
    typst = "typst"
    latex = "latex"


writer_classes = {
    SupportedTo.json: writers.JsonWriter,
    SupportedTo.latex: writers.LatexWriter,
    SupportedTo.typst: writers.TypstWriter,
}
