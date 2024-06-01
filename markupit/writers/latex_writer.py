from .writer import Writer
from .. import structure as st
from ..structure.document import Document


class LatexWriter(Writer):
    """A class representing a Latex writer for a document.

    :param input: The document to write.
    :type input: Document
    """

    def __init__(self, input: Document) -> None:
        super().__init__(input)

    def convert_space(self, obj: st.Inline.Space) -> str:
        return " "

    def convert_soft_break(self, obj: st.Inline.SoftBreak) -> str:
        return "\\"

    def convert_line_break(self, obj: st.Inline.LineBreak) -> str:
        return "\\par"

    def convert_str(self, obj: st.Inline.Str) -> str:
        return obj.content

    def convert_emph(self, obj: st.Inline.Emph) -> str:
        return f"\\emph{{{self.convert_element(obj.content)}}}"

    def convert_underline(self, obj: st.Inline.Underline) -> str:
        return f"\\underline{{{self.convert_element(obj.content)}}}"

    def convert_strong(self, obj: st.Inline.Strong) -> str:
        return f"\\textbf{{{self.convert_element(obj.content)}}}"

    def convert_strikeout(self, obj: st.Inline.Strikeout) -> str:
        return f"\\sout{{{self.convert_element(obj.content)}}}"

    def convert_superscript(self, obj: st.Inline.Superscript) -> str:
        return f"\\textsuperscript{{{self.convert_element(obj.content)}}}"

    def convert_subscript(self, obj: st.Inline.Subscript) -> str:
        return f"\\textsubscript{{{self.convert_element(obj.content)}}}"

    def convert_small_caps(self, obj: st.Inline.SmallCaps) -> str:
        return f"\\textsc{{{self.convert_element(obj.content)}}}"

    def convert_note(self, obj: st.Inline.Note) -> str:
        return f"\\footnote{{{self.convert_element(obj.content)}}}"

    def convert_link(self, obj: st.Inline.Link) -> str:
        return f"\\href{{{obj.content[2].content[0]}}}{{{self.convert_element(obj.content[1])}}}"

    def convert_image(self, obj: st.Inline.Image) -> str:
        # Simple include graphics in Latex has no alt text, this is skipped
        return f"\\includegraphics[width=0.25\\linewidth]{{{obj.content[2].content[0]}}}"

    def convert_code(self, obj: st.Inline.Code) -> str:
        return f"\\verb|{obj.content[1]}|"

    def convert_raw_inline(self, obj: st.Inline.RawInline) -> str:
        return f"\\verb|{obj.content[1]}|"

    def convert_horizontal_rule(self, obj: st.Block.HorizontalRule) -> str:
        return "noindent\\makebox[\\linewidth]{\\rule{\\paperwidth}{0.4pt}}"

    def convert_plain(self, obj: st.Block.Plain) -> str:
        block_content = "\n".join(obj.content)
        return f"\\begin{{verbatim}}\n{block_content}\n\\end{{verbatim}}\n"

    def convert_para(self, obj: st.Block.Para) -> str:
        return self.convert_element(obj.content) + "\n\n"

    def convert_block_quote(self, obj: st.Block.BlockQuote) -> str:
        return f"\\begin{{quote}}\n{self.convert_element(obj.content)}\n\\end{{quote}}\n"

    def convert_code_block(self, obj: st.Block.CodeBlock) -> str:
        block_content = "\n".join(obj.content)
        return f"\\begin{{verbatim}}\n{block_content}\n\\end{{verbatim}}\n"

    def convert_raw_block(self, obj: st.Block.RawBlock) -> str:
        # not supported in Latex
        pass

    def convert_header(self, obj: st.Block.Header) -> str:
        if obj.content[0] == 1:
            return f"\\section{{{self.convert_element(obj.content[2])}}}\n"
        if obj.content[0] == 2:
            return f"\\subsection{{{self.convert_element(obj.content[2])}}}\n"
        if obj.content[0] == 3:
            return f"\\subsubsection{{{self.convert_element(obj.content[2])}}}\n"
        if obj.content[0] == 4:
            return f"\\paragraph{{{self.convert_element(obj.content[2])}}}\n"
        if obj.content[0] == 5:
            return f"\\subparagraph{{{self.convert_element(obj.content[2])}}}\n"
        return self.convert_element(obj.content[2]) + "\n"

    def convert_table(self, obj: st.Block.Table) -> str:
        pass

    def convert_bullet_list(self, obj: st.Block.BulletList, nesting: int = 0) -> str:
        rows_txt = "\\begin{itemize}\n"
        for i in obj.content[0]:
            if isinstance(i, st.Block.BulletList):
                rows_txt += f"{self.convert_bullet_list(i, nesting + 1)}"
            elif isinstance(i, st.Block.OrderedList):
                rows_txt += f"{self.convert_ordered_list(i, nesting + 1)}"
            elif isinstance(i, st.Block.Plain) or isinstance(i, st.Block.Para):
                rows_txt += f"\\item {self.convert_element(i.content)}\n"
            else:
                rows_txt += f"\\item {self.convert_element(i)}\n"
        rows_txt += "\\end{itemize}\n"
        return rows_txt

    def convert_ordered_list(self, obj: st.Block.OrderedList, nesting: int = 0) -> str:
        # list attributes are not supported
        rows_txt = "\\begin{enumerate}\n"
        for i in obj.content[1][0]:
            if isinstance(i, st.Block.BulletList):
                rows_txt += f"{self.convert_bullet_list(i, nesting + 1)}"
            elif isinstance(i, st.Block.OrderedList):
                rows_txt += f"{self.convert_ordered_list(i, nesting + 1)}"
            elif isinstance(i, st.Block.Plain) or isinstance(i, st.Block.Para):
                rows_txt += f"\\item {self.convert_element(i.content)}\n"
            else:
                rows_txt += f"\\item {self.convert_element(i)}\n"
        rows_txt += "\\end{enumerate}\n"
        return rows_txt
