from .writer import Writer
from ..structure.document import Document
from .. import structure as st


class TypstWriter(Writer):
    def __init__(self, input: Document) -> None:
        super().__init__(input)
        self.nest_level = 0

    def convert_space(self, obj: st.Inline.Space) -> str:
        return " "

    def convert_soft_break(self, obj: st.Inline.SoftBreak) -> str:
        return " \\\n"

    def convert_line_break(self, obj: st.Inline.LineBreak) -> str:
        return "\n#parbreak()\n"

    def convert_str(self, obj: st.Inline.Str) -> str:
        return obj.content

    def convert_emph(self, obj: st.Inline.Emph) -> str:
        return f"#emph[{self.convert_element(obj.content)}]"

    def convert_underline(self, obj: st.Inline.Underline) -> str:
        return f"#underline[{self.convert_element(obj.content)}]"

    def convert_strong(self, obj: st.Inline.Strong) -> str:
        return f"#strong[{self.convert_element(obj.content)}]"

    def convert_strikeout(self, obj: st.Inline.Strikeout) -> str:
        return f"#strike[{self.convert_element(obj.content)}]"

    def convert_superscript(self, obj: st.Inline.Superscript) -> str:
        return f"#super[{self.convert_element(obj.content)}]"

    def convert_subscript(self, obj: st.Inline.Subscript) -> str:
        return f"#sub[{self.convert_element(obj.content)}]"

    def convert_small_caps(self, obj: st.Inline.SmallCaps) -> str:
        return f"#smallcaps({self.convert_element(obj.content)})"

    def convert_note(self, obj: st.Inline.Note) -> str:
        return f"#footnote[{self.convert_element(obj.content)}]"

    def convert_link(self, obj: st.Inline.Link) -> str:
        # Typst has no support for hover information, this is skipped
        return f'#link("{obj.content[1]}")[{self.convert_element(obj.content[1])}]'

    def convert_image(self, obj: st.Inline.Image) -> str:
        # Typst has no support for hover information, this is skipped
        alt = [self.convert_element(i) for i in obj.content[1]].join(" ")
        if alt != "":
            alt = f', alt: "{alt}"'
        return f'#figure(image("{obj.content[2][0]}"{alt})'

    def convert_code(self, obj: st.Inline.Code) -> str:
        return f"`{obj.code}`)"

    def convert_raw_inline(self, obj: st.Inline.RawInline) -> str:
        # not supported in Typst
        pass

    def convert_horizontal_rule(self, obj: st.Block.HorizontalRule) -> str:
        return "#line(length: 100%)\n"

    def convert_plain(self, obj: st.Block.Plain) -> str:
        # should be converted in other functions
        raise NotImplementedError("Plain block should be converted in other functions")

    def convert_para(self, obj: st.Block.Para) -> str:
        return self.convert_element(obj.content) + "\n\n"

    def convert_block_quote(self, obj: st.Block.BlockQuote) -> str:
        # not the best solution but Typst has no support for block quotes
        # you cannot format text in Typst inside a quote
        return f'#quote("{self.convert_element(obj.content)}")'

    def convert_code_block(self, obj: st.Block.CodeBlock) -> str:
        return f"\n```{obj.content[0][1][0]}\n{obj.content[1]}\n```\n"

    def convert_raw_block(self, obj: st.Block.RawBlock) -> str:
        # not supported in Typst
        pass

    def convert_header(self, obj: st.Block.Header) -> str:
        return f"\n{'=' * obj.content[0] + ' ' + self.convert_element(obj.content[2])}\n"

    def convert_table(self, obj: st.Block.Table) -> str:
        align_dict = {"AlignLeft": "left", "AlignRight": "right", "AlignCenter": "center", "AlignDefault": "auto"}
        columns = len(obj.content[2])
        align = [i[0] for i in obj.content[2]]
        align = [align_dict[i] for i in align]
        rows = obj.content[3][2] + obj.content[4][3]
        cells = [(self.convert_element(cell[4]) for cell in row[1]) for row in rows]
        cells_in_table = ("[" + i + "],\n" for i in cells)
        return f"""#align(center)[#table(
                    columns: {columns},
                    align: (col, row) => ({', '.join(align)}).at(col),
                    inset: 6pt,
                    {(cell for cell in cells_in_table).join("")}
                """

    def convert_bullet_list(self, obj: st.Block.BulletList, nesting: int = 0) -> str:
        rows_txt = ""
        for i in obj.content[0]:
            if isinstance(i, st.Block.BulletList):
                rows_txt += f"{self.convert_bullet_list(i, nesting + 1)}"
            elif isinstance(i, st.Block.OrderedList):
                rows_txt += f"{self.convert_ordered_list(i, nesting + 1)}"
            elif isinstance(i, st.Block.Plain) or isinstance(i, st.Block.Para):
                rows_txt += f"{'  '*nesting}- {self.convert_element(i.content)}\n"
            else:
                rows_txt += f"{'  '*nesting}- {self.convert_element(i)}\n"
        return rows_txt

    def convert_ordered_list(self, obj: st.Block.OrderedList, nesting: int = 0) -> str:
        # list attributes are not supported
        rows_txt = ""
        for i in obj.content[1][0]:
            if isinstance(i, st.Block.BulletList):
                rows_txt += f"{self.convert_bullet_list(i, nesting + 1)}"
            elif isinstance(i, st.Block.OrderedList):
                rows_txt += f"{self.convert_ordered_list(i, nesting + 1)}"
            elif isinstance(i, st.Block.Plain) or isinstance(i, st.Block.Para):
                rows_txt += f"{'  '*nesting}+ {self.convert_element(i.content)}\n"
            else:
                rows_txt += f"{'  '*nesting}+ {self.convert_element(i)}\n"
        return rows_txt
