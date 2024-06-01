import markup_converter.structure as ast
from markup_converter.writers.latex_writer import LatexWriter


def test_empty_document():
    doc = ast.Document()
    writer = LatexWriter(doc)
    assert writer.write() == ""


def test_convert_space():
    doc = ast.Document(blocks=[ast.Inline.Space()])
    writer = LatexWriter(doc)
    assert writer.write() == " "


def test_convert_soft_break():
    doc = ast.Document(blocks=[ast.Inline.SoftBreak()])
    writer = LatexWriter(doc)
    assert writer.write() == "\\"


def test_convert_link():
    doc = ast.Document(
        blocks=[
            ast.Inline.Link(
                [
                    ast.Content.Attr(["", [], []]),
                    [ast.Inline.Str("Hello")],
                    ast.Content.Target(["http://example.com", ""]),
                ]
            )
        ]
    )
    writer = LatexWriter(doc)
    assert writer.write() == "\\href{http://example.com}{Hello}"


def test_convert_code():
    doc = ast.Document(
        blocks=[
            ast.Inline.Code(
                [
                    ast.Content.Attr(["", [], []]),
                    "print('Hello, World!')",
                ]
            )
        ]
    )
    writer = LatexWriter(doc)
    assert writer.write() == "\\verb|print('Hello, World!')|"


def test_block_quote():
    doc = ast.Document(
        blocks=[
            ast.Block.BlockQuote(
                [
                    ast.Block.Para(
                        [
                            ast.Inline.Str("Hello,"),
                            ast.Inline.Space(),
                            ast.Inline.Str("world!"),
                            ast.Inline.SoftBreak(),
                            ast.Inline.Str("Hi"),
                        ]
                    ),
                ]
            )
        ]
    )
    writer = LatexWriter(doc)
    assert (
        writer.write()
        == """\\begin{quote}
Hello, world!\\Hi
\\end{quote}
"""
    )


def test_list():
    doc = ast.Document(
        blocks=[
            ast.Block.OrderedList(
                [
                    ast.Content.ListAttributes(
                        [1, ast.Enum.ListNumberStyle("Decimal"), ast.Enum.ListNumberDelim("Period")]
                    ),
                    [
                        [
                            ast.Block.Para([ast.Inline.Str("This is a list item.")]),
                            ast.Block.Para([ast.Inline.Str("This is another list item.")]),
                            ast.Block.BulletList(
                                [
                                    [
                                        ast.Block.Plain([ast.Inline.Str("This is a nested list item.")]),
                                        ast.Block.Plain([ast.Inline.Str("This is another nested list item.")]),
                                    ]
                                ]
                            ),
                        ]
                    ],
                ]
            )
        ]
    )
    writer = LatexWriter(doc)
    assert (
        writer.write()
        == """\\begin{enumerate}
\\item This is a list item.
\\item This is another list item.
\\begin{itemize}
\\item This is a nested list item.
\\item This is another nested list item.
\\end{itemize}
\\end{enumerate}
"""
    )
