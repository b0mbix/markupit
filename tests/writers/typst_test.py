import markup_converter.structure as ast
from markup_converter.writers import TypstWriter


def test_empty_document():
    doc = ast.Document()
    writer = TypstWriter(doc)
    assert writer.write() == ""


def test_convert_space():
    doc = ast.Document(blocks=[ast.Inline.Space()])
    writer = TypstWriter(doc)
    assert writer.write() == " "


def test_convert_soft_break():
    doc = ast.Document(blocks=[ast.Inline.SoftBreak()])
    writer = TypstWriter(doc)
    assert writer.write() == " \\\n"


def test_convert_para():
    doc = ast.Document(
        blocks=[
            ast.Block.Para(
                [
                    ast.Inline.Str("Hello,"),
                    ast.Inline.Space(),
                    ast.Inline.Str("world!"),
                    ast.Inline.SoftBreak(),
                    ast.Inline.Str("This"),
                    ast.Inline.Space(),
                    ast.Inline.Str("is"),
                    ast.Inline.Space(),
                    ast.Inline.Emph([ast.Inline.Str("a")]),
                    ast.Inline.Space(),
                    ast.Inline.Str("test"),
                    ast.Inline.Space(),
                    ast.Inline.Str("document."),
                ]
            )
        ]
    )
    writer = TypstWriter(doc)
    assert writer.write() == "Hello, world! \\\nThis is #emph[a] test document.\n\n"


def test_convert_header():
    doc = ast.Document(blocks=[ast.Block.Header([1, ast.Content.Attr(["", [], []]), [ast.Inline.Str("Hello")]])])
    writer = TypstWriter(doc)
    assert writer.write() == "\n= Hello\n"


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
    writer = TypstWriter(doc)
    assert (
        writer.write()
        == """+ This is a list item.
+ This is another list item.
  - This is a nested list item.
  - This is another nested list item.
"""
    )
