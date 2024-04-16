from pytest import raises

import markup_converter.markup_ast as ast


def test_empty_document():
    blocks = ast.Document()
    assert blocks.to_json() == {"blocks": []}


def test_document_with_blocks():
    blocks = ast.Document()
    blocks.add_block(ast.Inline("Str", "Hello"))
    blocks.add_block(ast.Inline("Space"))
    blocks.add_block(ast.Inline("Str", "World!"))

    assert blocks.to_json() == {
        "blocks": [
            {"t": "Str", "c": "Hello"},
            {"t": "Space"},
            {"t": "Str", "c": "World!"},
        ]
    }


def test_document_with_nested_blocks():
    blocks = ast.Document()
    blocks.add_block(ast.Inline("Str", "Hello"))
    blocks.add_block(ast.Inline("Space"))
    strong = ast.Inline("Strong", [ast.Inline("Str", "World!")])
    blocks.add_block(strong)

    assert blocks.to_json() == {
        "blocks": [{"t": "Str", "c": "Hello"}, {"t": "Space"}, {"t": "Strong", "c": [{"t": "Str", "c": "World!"}]}]
    }


def test_content_for_non_content_types_error():
    with raises(ValueError):
        ast.Inline("Space", "Hello")
    with raises(ValueError):
        ast.Inline("SoftBreak", ast.Inline("Str", " "))
    with raises(ValueError):
        ast.Inline("LineBreak", "World")


def test_str_content_error():
    with raises(ValueError):
        ast.Inline("Str")
    with raises(ValueError):
        ast.Inline("Str", 1)
    with raises(ValueError):
        ast.Inline("Str", ast.Inline("Str", "Hello"))
