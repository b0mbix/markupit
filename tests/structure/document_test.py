from pytest import raises

import markupit.structure as ast


def test_empty_document():
    blocks = ast.Document()
    assert blocks.to_json() == {"blocks": []}


def test_document_add_block():
    blocks = ast.Document()
    blocks.add_block(ast.Inline.Str("Hello"))
    blocks.add_block(ast.Inline.Space())
    blocks.add_block(ast.Inline.Str("World!"))

    assert blocks.to_json() == {
        "blocks": [
            {"t": "Str", "c": "Hello"},
            {"t": "Space"},
            {"t": "Str", "c": "World!"},
        ]
    }


def test_document_add_block_nested():
    blocks = ast.Document()
    blocks.add_block(ast.Inline.Str("Hello"))
    blocks.add_block(ast.Inline.Space())
    strong = ast.Inline.Strong([ast.Inline.Str("World!")])
    blocks.add_block(strong)

    assert blocks.to_json() == {
        "blocks": [{"t": "Str", "c": "Hello"}, {"t": "Space"}, {"t": "Strong", "c": [{"t": "Str", "c": "World!"}]}]
    }


def test_document_add_block_incorrect():
    blocks = ast.Document()
    with raises(TypeError):
        blocks.add_block("Hello")
    with raises(TypeError):
        blocks.add_block(ast.Inline.Str("Hello"), ast.Inline.Space(), ast.Inline.Str("World!"))
    with raises(TypeError):
        blocks.add_block(["Hello", ast.Inline.Space(), ast.Inline.Str("World!")])


def test_document_add_blocks():
    blocks = ast.Document()
    blocks.add_blocks([ast.Inline.Str("Hello"), ast.Inline.Space(), ast.Inline.Str("World!")])

    assert blocks.to_json() == {
        "blocks": [
            {"t": "Str", "c": "Hello"},
            {"t": "Space"},
            {"t": "Str", "c": "World!"},
        ]
    }


def test_document_add_blocks_nested():
    blocks = ast.Document()
    blocks.add_blocks([ast.Inline.Str("Hello"), ast.Inline.Space(), ast.Inline.Strong([ast.Inline.Str("World!")])])

    assert blocks.to_json() == {
        "blocks": [{"t": "Str", "c": "Hello"}, {"t": "Space"}, {"t": "Strong", "c": [{"t": "Str", "c": "World!"}]}]
    }


def test_document_add_blocks_incorrect():
    blocks = ast.Document()
    with raises(TypeError):
        blocks.add_blocks("Hello")
    with raises(TypeError):
        blocks.add_blocks(ast.Inline.Str("Hello"), ast.Inline.Space(), ast.Inline.Str("World!"))
    with raises(TypeError):
        blocks.add_blocks(["Hello", ast.Inline.Space(), ast.Inline.Str("World!")])
    with raises(TypeError):
        blocks.add_blocks(["Hello", "World!"])


def test_document_with_blocks_as_args():
    blocks = ast.Document(
        [
            ast.Inline.Str("Hello"),
            ast.Inline.Space(),
            ast.Inline.Str("World!"),
        ]
    )

    assert blocks.to_json() == {
        "blocks": [
            {"t": "Str", "c": "Hello"},
            {"t": "Space"},
            {"t": "Str", "c": "World!"},
        ]
    }


def test_document_with_blocks_as_args_nested():
    blocks = ast.Document(
        [
            ast.Inline.Str("Hello"),
            ast.Inline.Space(),
            ast.Inline.Strong([ast.Inline.Str("World!")]),
        ]
    )

    assert blocks.to_json() == {
        "blocks": [{"t": "Str", "c": "Hello"}, {"t": "Space"}, {"t": "Strong", "c": [{"t": "Str", "c": "World!"}]}]
    }


def test_document_with_incorrect_args():
    with raises(TypeError):
        ast.Document("Hello")
    with raises(TypeError):
        ast.Document([ast.Inline.Str("Hello"), "World!"])
    with raises(TypeError):
        ast.Document(["Hello", "World!"])
    with raises(TypeError):
        ast.Document("Hello", "World!")


def test_document_init_with_args_and_add_block():
    blocks = ast.Document([ast.Inline.Str("Hello")])
    blocks.add_block(ast.Inline.Space())
    blocks.add_block(ast.Inline.Str("World!"))

    assert blocks.to_json() == {
        "blocks": [
            {"t": "Str", "c": "Hello"},
            {"t": "Space"},
            {"t": "Str", "c": "World!"},
        ]
    }


def test_document_init_with_args_and_add_blocks():
    blocks = ast.Document([ast.Inline.Str("Hello")])
    blocks.add_blocks([ast.Inline.Space(), ast.Inline.Str("World!")])

    assert blocks.to_json() == {
        "blocks": [
            {"t": "Str", "c": "Hello"},
            {"t": "Space"},
            {"t": "Str", "c": "World!"},
        ]
    }
