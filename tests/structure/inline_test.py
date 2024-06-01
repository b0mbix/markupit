from pytest import raises

import markupit.structure as ast


def test_non_content_types():
    assert ast.Inline.Space().to_json() == {"t": "Space"}
    assert ast.Inline.SoftBreak().to_json() == {"t": "SoftBreak"}
    assert ast.Inline.LineBreak().to_json() == {"t": "LineBreak"}


def test_content_for_non_content_types_error():
    with raises(TypeError):
        ast.Inline.Space("Hello")
    with raises(TypeError):
        ast.Inline.SoftBreak(ast.Inline.Str(" "))
    with raises(TypeError):
        ast.Inline.LineBreak("World")


def test_str():
    assert ast.Inline.Str("Hello").to_json() == {"t": "Str", "c": "Hello"}
    assert ast.Inline.Str("World!").to_json() == {"t": "Str", "c": "World!"}


def test_str_content_error():
    with raises(TypeError):
        ast.Inline.Str()
    with raises(TypeError):
        ast.Inline.Str(1)
    with raises(TypeError):
        ast.Inline.Str(ast.Inline.Str("Hello"))


def test_emph():
    assert ast.Inline.Emph([ast.Inline.Str("Hello")]).to_json() == {"t": "Emph", "c": [{"t": "Str", "c": "Hello"}]}
    assert ast.Inline.Emph([ast.Inline.Space()]).to_json() == {"t": "Emph", "c": [{"t": "Space"}]}
    assert ast.Inline.Emph([ast.Inline.Str("World!")]).to_json() == {"t": "Emph", "c": [{"t": "Str", "c": "World!"}]}
    assert ast.Inline.Emph([ast.Inline.Str("Hello"), ast.Inline.Space(), ast.Inline.Str("World!")]).to_json() == {
        "t": "Emph",
        "c": [
            {"t": "Str", "c": "Hello"},
            {"t": "Space"},
            {"t": "Str", "c": "World!"},
        ],
    }


def test_emph_content_error():
    with raises(TypeError):
        ast.Inline.Emph()
    with raises(TypeError):
        ast.Inline.Emph("Hello")
    with raises(TypeError):
        ast.Inline.Emph(ast.Inline.Emph("Hello"))
    with raises(TypeError):
        ast.Inline.Emph([ast.Block.Para([ast.Inline.Str("Hello")])])
    with raises(TypeError):
        ast.Inline.Emph([ast.Inline.Str("Hello"), " ", ast.Inline.Str("World!")])


def test_underline():
    assert ast.Inline.Underline([ast.Inline.Str("Hello")]).to_json() == {
        "t": "Underline",
        "c": [{"t": "Str", "c": "Hello"}],
    }
    assert ast.Inline.Underline([ast.Inline.Space()]).to_json() == {"t": "Underline", "c": [{"t": "Space"}]}
    assert ast.Inline.Underline([ast.Inline.Str("World!")]).to_json() == {
        "t": "Underline",
        "c": [{"t": "Str", "c": "World!"}],
    }
    assert ast.Inline.Underline([ast.Inline.Str("Hello"), ast.Inline.Space(), ast.Inline.Str("World!")]).to_json() == {
        "t": "Underline",
        "c": [
            {"t": "Str", "c": "Hello"},
            {"t": "Space"},
            {"t": "Str", "c": "World!"},
        ],
    }


def test_underline_content_error():
    with raises(TypeError):
        ast.Inline.Underline()
    with raises(TypeError):
        ast.Inline.Underline("Hello")
    with raises(TypeError):
        ast.Inline.Underline(ast.Inline.Underline("Hello"))
    with raises(TypeError):
        ast.Inline.Underline([ast.Block.Para([ast.Inline.Str("Hello")])])
    with raises(TypeError):
        ast.Inline.Underline([ast.Inline.Str("Hello"), " ", ast.Inline.Str("World!")])


def test_strong():
    assert ast.Inline.Strong([ast.Inline.Str("Hello")]).to_json() == {
        "t": "Strong",
        "c": [{"t": "Str", "c": "Hello"}],
    }
    assert ast.Inline.Strong([ast.Inline.Space()]).to_json() == {"t": "Strong", "c": [{"t": "Space"}]}
    assert ast.Inline.Strong([ast.Inline.Str("World!")]).to_json() == {
        "t": "Strong",
        "c": [{"t": "Str", "c": "World!"}],
    }
    assert ast.Inline.Strong([ast.Inline.Str("Hello"), ast.Inline.Space(), ast.Inline.Str("World!")]).to_json() == {
        "t": "Strong",
        "c": [
            {"t": "Str", "c": "Hello"},
            {"t": "Space"},
            {"t": "Str", "c": "World!"},
        ],
    }


def test_strong_content_error():
    with raises(TypeError):
        ast.Inline.Strong()
    with raises(TypeError):
        ast.Inline.Strong("Hello")
    with raises(TypeError):
        ast.Inline.Strong(ast.Inline.Strong("Hello"))
    with raises(TypeError):
        ast.Inline.Strong([ast.Block.Para([ast.Inline.Str("Hello")])])
    with raises(TypeError):
        ast.Inline.Strong([ast.Inline.Str("Hello"), " ", ast.Inline.Str("World!")])


def test_strikeout():
    assert ast.Inline.Strikeout([ast.Inline.Str("Hello")]).to_json() == {
        "t": "Strikeout",
        "c": [{"t": "Str", "c": "Hello"}],
    }
    assert ast.Inline.Strikeout([ast.Inline.Space()]).to_json() == {"t": "Strikeout", "c": [{"t": "Space"}]}
    assert ast.Inline.Strikeout([ast.Inline.Str("World!")]).to_json() == {
        "t": "Strikeout",
        "c": [{"t": "Str", "c": "World!"}],
    }
    assert ast.Inline.Strikeout([ast.Inline.Str("Hello"), ast.Inline.Space(), ast.Inline.Str("World!")]).to_json() == {
        "t": "Strikeout",
        "c": [
            {"t": "Str", "c": "Hello"},
            {"t": "Space"},
            {"t": "Str", "c": "World!"},
        ],
    }


def test_strikeout_content_error():
    with raises(TypeError):
        ast.Inline.Strikeout()
    with raises(TypeError):
        ast.Inline.Strikeout("Hello")
    with raises(TypeError):
        ast.Inline.Strikeout(ast.Inline.Strikeout("Hello"))
    with raises(TypeError):
        ast.Inline.Strikeout([ast.Block.Para([ast.Inline.Str("Hello")])])
    with raises(TypeError):
        ast.Inline.Strikeout([ast.Inline.Str("Hello"), " ", ast.Inline.Str("World!")])


def test_superscript():
    assert ast.Inline.Superscript([ast.Inline.Str("Hello")]).to_json() == {
        "t": "Superscript",
        "c": [{"t": "Str", "c": "Hello"}],
    }
    assert ast.Inline.Superscript([ast.Inline.Space()]).to_json() == {"t": "Superscript", "c": [{"t": "Space"}]}
    assert ast.Inline.Superscript([ast.Inline.Str("World!")]).to_json() == {
        "t": "Superscript",
        "c": [{"t": "Str", "c": "World!"}],
    }
    assert ast.Inline.Superscript(
        [ast.Inline.Str("Hello"), ast.Inline.Space(), ast.Inline.Str("World!")]
    ).to_json() == {
        "t": "Superscript",
        "c": [
            {"t": "Str", "c": "Hello"},
            {"t": "Space"},
            {"t": "Str", "c": "World!"},
        ],
    }


def test_superscript_content_error():
    with raises(TypeError):
        ast.Inline.Superscript()
    with raises(TypeError):
        ast.Inline.Superscript("Hello")
    with raises(TypeError):
        ast.Inline.Superscript(ast.Inline.Superscript("Hello"))
    with raises(TypeError):
        ast.Inline.Superscript([ast.Block.Para([ast.Inline.Str("Hello")])])
    with raises(TypeError):
        ast.Inline.Superscript([ast.Inline.Str("Hello"), " ", ast.Inline.Str("World!")])


def test_subscript():
    assert ast.Inline.Subscript([ast.Inline.Str("Hello")]).to_json() == {
        "t": "Subscript",
        "c": [{"t": "Str", "c": "Hello"}],
    }
    assert ast.Inline.Subscript([ast.Inline.Space()]).to_json() == {"t": "Subscript", "c": [{"t": "Space"}]}
    assert ast.Inline.Subscript([ast.Inline.Str("World!")]).to_json() == {
        "t": "Subscript",
        "c": [{"t": "Str", "c": "World!"}],
    }
    assert ast.Inline.Subscript([ast.Inline.Str("Hello"), ast.Inline.Space(), ast.Inline.Str("World!")]).to_json() == {
        "t": "Subscript",
        "c": [
            {"t": "Str", "c": "Hello"},
            {"t": "Space"},
            {"t": "Str", "c": "World!"},
        ],
    }


def test_subscript_content_error():
    with raises(TypeError):
        ast.Inline.Subscript()
    with raises(TypeError):
        ast.Inline.Subscript("Hello")
    with raises(TypeError):
        ast.Inline.Subscript(ast.Inline.Subscript("Hello"))
    with raises(TypeError):
        ast.Inline.Subscript([ast.Block.Para([ast.Inline.Str("Hello")])])
    with raises(TypeError):
        ast.Inline.Subscript([ast.Inline.Str("Hello"), " ", ast.Inline.Str("World!")])


def test_small_caps():
    assert ast.Inline.SmallCaps([ast.Inline.Str("Hello")]).to_json() == {
        "t": "SmallCaps",
        "c": [{"t": "Str", "c": "Hello"}],
    }
    assert ast.Inline.SmallCaps([ast.Inline.Space()]).to_json() == {"t": "SmallCaps", "c": [{"t": "Space"}]}
    assert ast.Inline.SmallCaps([ast.Inline.Str("World!")]).to_json() == {
        "t": "SmallCaps",
        "c": [{"t": "Str", "c": "World!"}],
    }
    assert ast.Inline.SmallCaps([ast.Inline.Str("Hello"), ast.Inline.Space(), ast.Inline.Str("World!")]).to_json() == {
        "t": "SmallCaps",
        "c": [
            {"t": "Str", "c": "Hello"},
            {"t": "Space"},
            {"t": "Str", "c": "World!"},
        ],
    }


def test_small_caps_content_error():
    with raises(TypeError):
        ast.Inline.SmallCaps()
    with raises(TypeError):
        ast.Inline.SmallCaps("Hello")
    with raises(TypeError):
        ast.Inline.SmallCaps(ast.Inline.SmallCaps("Hello"))
    with raises(TypeError):
        ast.Inline.SmallCaps([ast.Block.Para([ast.Inline.Str("Hello")])])
    with raises(TypeError):
        ast.Inline.SmallCaps([ast.Inline.Str("Hello"), " ", ast.Inline.Str("World!")])


def test_note():
    assert ast.Inline.Note([ast.Block.Para([ast.Inline.Str("Hello")])]).to_json() == {
        "t": "Note",
        "c": [{"t": "Para", "c": [{"t": "Str", "c": "Hello"}]}],
    }
    assert ast.Inline.Note([ast.Block.Para([ast.Inline.Space()])]).to_json() == {
        "t": "Note",
        "c": [{"t": "Para", "c": [{"t": "Space"}]}],
    }
    assert ast.Inline.Note([ast.Block.Para([ast.Inline.Str("World!")])]).to_json() == {
        "t": "Note",
        "c": [{"t": "Para", "c": [{"t": "Str", "c": "World!"}]}],
    }
    assert ast.Inline.Note(
        [ast.Block.Para([ast.Inline.Str("Hello"), ast.Inline.Space(), ast.Inline.Str("World!")])]
    ).to_json() == {
        "t": "Note",
        "c": [
            {
                "t": "Para",
                "c": [
                    {"t": "Str", "c": "Hello"},
                    {"t": "Space"},
                    {"t": "Str", "c": "World!"},
                ],
            }
        ],
    }
    assert ast.Inline.Note(
        [ast.Block.Para([ast.Inline.Str("Hello")]), ast.Block.Para([ast.Inline.Str("World!")])]
    ).to_json() == {
        "t": "Note",
        "c": [
            {"t": "Para", "c": [{"t": "Str", "c": "Hello"}]},
            {"t": "Para", "c": [{"t": "Str", "c": "World!"}]},
        ],
    }


def test_note_content_error():
    with raises(TypeError):
        ast.Inline.Note()
    with raises(TypeError):
        ast.Inline.Note("Hello")
    with raises(TypeError):
        ast.Inline.Note(ast.Inline.Note("Hello"))
    with raises(TypeError):
        ast.Inline.Note([ast.Inline.Str("Hello")])
    with raises(TypeError):
        ast.Inline.Note([ast.Inline.Str("Hello"), " ", ast.Inline.Str("World!")])
    with raises(TypeError):
        ast.Inline.Note([ast.Block.Para([ast.Inline.Str("Hello")]), ast.Inline.Str("World!")])
    with raises(TypeError):
        ast.Inline.Note(ast.Block.Para([ast.Inline.Str("Hello")]))


def test_span():
    assert ast.Inline.Span(
        [ast.Content.Attr(["id", ["class"], [["key", "value"]]]), [ast.Inline.Str("Hello")]]
    ).to_json() == {
        "t": "Span",
        "c": [
            {"t": "Attr", "c": ["id", ["class"], [["key", "value"]]]},
            [{"t": "Str", "c": "Hello"}],
        ],
    }
    assert ast.Inline.Span(
        [ast.Content.Attr(["id", ["class"], [["key", "value"]]]), [ast.Inline.Space()]]
    ).to_json() == {
        "t": "Span",
        "c": [
            {"t": "Attr", "c": ["id", ["class"], [["key", "value"]]]},
            [{"t": "Space"}],
        ],
    }
    assert ast.Inline.Span(
        [
            ast.Content.Attr(["id", ["class"], [["key", "value"]]]),
            [ast.Inline.Str("Hello"), ast.Inline.Space(), ast.Inline.Str("World!")],
        ]
    ).to_json() == {
        "t": "Span",
        "c": [
            {"t": "Attr", "c": ["id", ["class"], [["key", "value"]]]},
            [
                {"t": "Str", "c": "Hello"},
                {"t": "Space"},
                {"t": "Str", "c": "World!"},
            ],
        ],
    }


def test_span_content_error():
    with raises(TypeError):
        ast.Inline.Span()
    with raises(TypeError):
        ast.Inline.Span("Hello")
    with raises(TypeError):
        ast.Inline.Span(ast.Inline.Span("Hello"))
    with raises(TypeError):
        ast.Inline.Span([ast.Inline.Str("Hello")])
    with raises(TypeError):
        ast.Inline.Span([ast.Inline.Str("Hello"), " ", ast.Inline.Str("World!")])
    with raises(TypeError):
        ast.Inline.Span([ast.Block.Para([ast.Inline.Str("Hello")]), ast.Inline.Str("World!")])
    with raises(TypeError):
        ast.Inline.Span(ast.Block.Para([ast.Inline.Str("Hello")]))


def test_quoted():
    assert ast.Inline.Quoted([ast.Enum.QuoteType("SingleQuote"), [ast.Inline.Str("Hello")]]).to_json() == {
        "t": "Quoted",
        "c": [
            {"t": "SingleQuote"},
            [{"t": "Str", "c": "Hello"}],
        ],
    }
    assert ast.Inline.Quoted([ast.Enum.QuoteType("DoubleQuote"), [ast.Inline.Space()]]).to_json() == {
        "t": "Quoted",
        "c": [
            {"t": "DoubleQuote"},
            [{"t": "Space"}],
        ],
    }
    assert ast.Inline.Quoted(
        [ast.Enum.QuoteType("SingleQuote"), [ast.Inline.Str("Hello"), ast.Inline.Space(), ast.Inline.Str("World!")]]
    ).to_json() == {
        "t": "Quoted",
        "c": [
            {"t": "SingleQuote"},
            [
                {"t": "Str", "c": "Hello"},
                {"t": "Space"},
                {"t": "Str", "c": "World!"},
            ],
        ],
    }


def test_quoted_content_error():
    with raises(TypeError):
        ast.Inline.Quoted()
    with raises(TypeError):
        ast.Inline.Quoted("Hello")
    with raises(TypeError):
        ast.Inline.Quoted(ast.Inline.Quoted("Hello"))
    with raises(TypeError):
        ast.Inline.Quoted([ast.Inline.Str("Hello")])
    with raises(TypeError):
        ast.Inline.Quoted([ast.Inline.Str("Hello"), " ", ast.Inline.Str("World!")])
    with raises(TypeError):
        ast.Inline.Quoted([ast.Block.Para([ast.Inline.Str("Hello")]), ast.Inline.Str("World!")])
    with raises(TypeError):
        ast.Inline.Quoted(ast.Block.Para([ast.Inline.Str("Hello")]))


def test_link():
    assert ast.Inline.Link(
        [
            ast.Content.Attr(["", [], []]),
            [ast.Inline.Str("Hello")],
            ast.Content.Target(["http://example.com", ""]),
        ]
    ).to_json() == {
        "t": "Link",
        "c": [
            {"t": "Attr", "c": ["", [], []]},
            [{"t": "Str", "c": "Hello"}],
            {"t": "Target", "c": ["http://example.com", ""]},
        ],
    }
    assert ast.Inline.Link(
        [
            ast.Content.Attr(["", [], []]),
            [ast.Inline.Space()],
            ast.Content.Target(["http://example.com", ""]),
        ]
    ).to_json() == {
        "t": "Link",
        "c": [
            {"t": "Attr", "c": ["", [], []]},
            [{"t": "Space"}],
            {"t": "Target", "c": ["http://example.com", ""]},
        ],
    }
    assert ast.Inline.Link(
        [
            ast.Content.Attr(["id", ["class"], [["key", "value"]]]),
            [ast.Inline.Str("Hello"), ast.Inline.Space(), ast.Inline.Str("World!")],
            ast.Content.Target(["http://example.com", ""]),
        ]
    ).to_json() == {
        "t": "Link",
        "c": [
            {"t": "Attr", "c": ["id", ["class"], [["key", "value"]]]},
            [
                {"t": "Str", "c": "Hello"},
                {"t": "Space"},
                {"t": "Str", "c": "World!"},
            ],
            {"t": "Target", "c": ["http://example.com", ""]},
        ],
    }


def test_link_content_error():
    with raises(TypeError):
        ast.Inline.Link()
    with raises(TypeError):
        ast.Inline.Link("Hello")
    with raises(TypeError):
        ast.Inline.Link(ast.Inline.Link("Hello"))
    with raises(TypeError):
        ast.Inline.Link([ast.Inline.Str("Hello")])
    with raises(TypeError):
        ast.Inline.Link([ast.Inline.Str("Hello"), " ", ast.Inline.Str("World!")])
    with raises(TypeError):
        ast.Inline.Link([ast.Block.Para([ast.Inline.Str("Hello")]), ast.Inline.Str("World!")])
    with raises(TypeError):
        ast.Inline.Link(ast.Block.Para([ast.Inline.Str("Hello")]))


def test_image():
    assert ast.Inline.Image(
        [
            ast.Content.Attr(["", [], []]),
            [ast.Inline.Str("Hello")],
            ast.Content.Target(["Untitled.png", ""]),
        ]
    ).to_json() == {
        "t": "Image",
        "c": [
            {"t": "Attr", "c": ["", [], []]},
            [{"t": "Str", "c": "Hello"}],
            {"t": "Target", "c": ["Untitled.png", ""]},
        ],
    }
    assert ast.Inline.Image(
        [
            ast.Content.Attr(["id", ["class"], [["key", "value"]]]),
            [ast.Inline.Str("Hello"), ast.Inline.Space(), ast.Inline.Str("World!")],
            ast.Content.Target(["http://example.com/icon.png", ""]),
        ]
    ).to_json() == {
        "t": "Image",
        "c": [
            {"t": "Attr", "c": ["id", ["class"], [["key", "value"]]]},
            [
                {"t": "Str", "c": "Hello"},
                {"t": "Space"},
                {"t": "Str", "c": "World!"},
            ],
            {"t": "Target", "c": ["http://example.com/icon.png", ""]},
        ],
    }


def test_image_content_error():
    with raises(TypeError):
        ast.Inline.Image()
    with raises(TypeError):
        ast.Inline.Image("Hello")
    with raises(TypeError):
        ast.Inline.Image(ast.Inline.Image("Hello"))
    with raises(TypeError):
        ast.Inline.Image([ast.Inline.Str("Hello")])
    with raises(TypeError):
        ast.Inline.Image([ast.Inline.Str("Hello"), " ", ast.Inline.Str("World!")])
    with raises(TypeError):
        ast.Inline.Image([ast.Block.Para([ast.Inline.Str("Hello")]), ast.Inline.Str("World!")])
    with raises(TypeError):
        ast.Inline.Image(ast.Block.Para([ast.Inline.Str("Hello")]))


def test_code():
    assert ast.Inline.Code(
        [
            ast.Content.Attr(["", [], []]),
            "print('Hello, World!')",
        ]
    ).to_json() == {
        "t": "Code",
        "c": [
            {"t": "Attr", "c": ["", [], []]},
            "print('Hello, World!')",
        ],
    }
    assert ast.Inline.Code(
        [
            ast.Content.Attr(["id", ["class"], [["key", "value"]]]),
            "print('Hello, World!')",
        ]
    ).to_json() == {
        "t": "Code",
        "c": [
            {"t": "Attr", "c": ["id", ["class"], [["key", "value"]]]},
            "print('Hello, World!')",
        ],
    }


def test_code_content_error():
    with raises(TypeError):
        ast.Inline.Code()
    with raises(TypeError):
        ast.Inline.Code("Hello")
    with raises(TypeError):
        ast.Inline.Code(ast.Inline.Code("Hello"))
    with raises(TypeError):
        ast.Inline.Code([ast.Inline.Str("Hello")])
    with raises(TypeError):
        ast.Inline.Code([ast.Inline.Str("Hello"), " ", ast.Inline.Str("World!")])
    with raises(TypeError):
        ast.Inline.Code([ast.Block.Para([ast.Inline.Str("Hello")]), ast.Inline.Str("World!")])
    with raises(TypeError):
        ast.Inline.Code(ast.Block.Para([ast.Inline.Str("Hello")]))


def test_math():
    assert ast.Inline.Math(
        [
            ast.Enum.MathType("InlineMath"),
            "f(x) = x^2",
        ]
    ).to_json() == {
        "t": "Math",
        "c": [
            {"t": "InlineMath"},
            "f(x) = x^2",
        ],
    }
    assert ast.Inline.Math(
        [
            ast.Enum.MathType("DisplayMath"),
            "f(x) = x^2",
        ]
    ).to_json() == {
        "t": "Math",
        "c": [
            {"t": "DisplayMath"},
            "f(x) = x^2",
        ],
    }


def test_math_content_error():
    with raises(TypeError):
        ast.Inline.Math()
    with raises(TypeError):
        ast.Inline.Math("Hello")
    with raises(TypeError):
        ast.Inline.Math(ast.Inline.Math("Hello"))
    with raises(TypeError):
        ast.Inline.Math([ast.Inline.Str("Hello")])
    with raises(TypeError):
        ast.Inline.Math([ast.Inline.Str("Hello"), " ", ast.Inline.Str("World!")])
    with raises(TypeError):
        ast.Inline.Math([ast.Block.Para([ast.Inline.Str("Hello")]), ast.Inline.Str("World!")])
    with raises(TypeError):
        ast.Inline.Math(ast.Block.Para([ast.Inline.Str("Hello")]))


def test_raw_inline():
    assert ast.Inline.RawInline(
        [
            ast.Content.Format("html"),
            "<strong>Hello, World!</strong>",
        ]
    ).to_json() == {
        "t": "RawInline",
        "c": [
            "html",
            "<strong>Hello, World!</strong>",
        ],
    }
    assert ast.Inline.RawInline(
        [
            ast.Content.Format("tex"),
            r"\textbf{Hello, World!}",
        ]
    ).to_json() == {
        "t": "RawInline",
        "c": [
            "tex",
            r"\textbf{Hello, World!}",
        ],
    }


def test_raw_inline_content_error():
    with raises(TypeError):
        ast.Inline.RawInline()
    with raises(TypeError):
        ast.Inline.RawInline("Hello")
    with raises(TypeError):
        ast.Inline.RawInline(ast.Inline.RawInline("Hello"))
    with raises(TypeError):
        ast.Inline.RawInline([ast.Inline.Str("Hello")])
    with raises(TypeError):
        ast.Inline.RawInline([ast.Inline.Str("Hello"), " ", ast.Inline.Str("World!")])
    with raises(TypeError):
        ast.Inline.RawInline([ast.Block.Para([ast.Inline.Str("Hello")]), ast.Inline.Str("World!")])
    with raises(TypeError):
        ast.Inline.RawInline(ast.Block.Para([ast.Inline.Str("Hello")]))


# @TODO tests for Cite
