
How readers work?
=================

Readers are the main entry point for the library. They are responsible for converting the input document into our *AST* (*Abstract Syntax Tree*) representation. All of the readers are stored under the `readers` directory.

Before diving into the implementation details, let's first understand the basic structure of the readers.

Each reader itself is divided into two parts:
    - ``Block Parser`` - responsible for parsing the input document into larger blocks of text. For example, in markdown, a block parser would be responsible for parsing a paragraph, a list, a code block, etc.
    - ``Block Reader`` - responsible for converting the block of text into a block of *AST* nodes. For example, in markdown, a block reader would be responsible for converting a paragraph into a `Paragraph` node with a list of `Str`, `Emphasis`, `Strong`, etc. children nodes.

As it can be seen, we're following a two-step process:
    - First, we parse the input document into blocks of text.
    - Then, we convert these blocks of text into *AST* nodes.

This two-step process was inspired by `GFM authors <https://github.github.com/gfm/#appendix-a-parsing-strategy>`_. It allows us to write simplier and more modular code. It also allows us to easily extend the library by adding new block parsers and block readers.

So, how to create a custom reader?

For simplicity, we've created some core classes that you can use to create your own reader. Here their brief overview:
    - ``State`` - a class that holds the current state of the reader. It contains the input document, the current position and the current parsed blocks.
    - ``BaseParser`` - this is a base class for all block parsers. It have predefined methods for working with the state and defining grammar rules of blocks.
    - ``Reader`` - this is an interface that defines the main methods for the reader. It contains the `read` and `read_file` methods that take the input document and return the *AST* representation of the document.

To create a custom reader, you need to define 3 classes:
    - ``CustomBlockParser`` - a class that inherits from `BaseParser` and defines the grammar rules for the blocks.
    - ``CustomBlockReader`` - a class that converts the block of text into a block of *AST* nodes.
    - ``CustomReader`` - a class that inherits from `Reader` and defines the `read` method.

