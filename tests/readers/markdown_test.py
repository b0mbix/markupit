import markup_converter.structure as ast
from markup_converter.readers import MarkdownReader


def text_list():
    md = """
1. outer
    + inner
    + inner
2. outer
"""
    reader = MarkdownReader()
    doc = reader.read(md)
    assert doc.blocks == [
        ast.Block.OrderedList(
            [
                ast.Content.ListAttributes(
                    [
                        1,
                        ast.Content.ListAttributes(["", [], []]),
                        [
                            ast.Block.ListItem(
                                [
                                    ast.Block.Plain(
                                        [
                                            ast.Inline.Str("outer"),
                                            ast.Inline.SoftBreak(),
                                            ast.Inline.Str("inner"),
                                            ast.Inline.SoftBreak(),
                                            ast.Inline.Str("inner"),
                                        ]
                                    )
                                ]
                            )
                        ],
                    ]
                )
            ]
        ),
        ast.Block.OrderedList(
            [
                ast.Content.ListAttributes(
                    [
                        2,
                        ast.Content.ListAttributes(["", [], []]),
                        [ast.Block.ListItem([ast.Block.Plain([ast.Inline.Str("outer")])])],
                    ]
                )
            ]
        ),
    ]
