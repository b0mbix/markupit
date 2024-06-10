
How writers work?
=================

In our program, we use writers to export structure written in Python to a markup file. All of the writers are stored in the `writers` file.

There is an abstract class defining the basic way a writer works. In this class, there are the following core functions:

- ``write`` - converts a document into a string with the content of the markup file
- ``write_file`` - converts a document and writes it into a markup file
- ``convert_element`` - finds and performs a converting action for an Element or an array of Elements

This is the core of every writer and generally it should not be changed.

Based on this core, we can create our custom writers. The only thing we have to do is to write a proper text representation of each element. For instance, this is the `convert_strong` function in `TypstWriter`:

.. code-block:: python

    def convert_strong(self, obj: st.Inline.Strong) -> str:
        return f"#strong[{self.convert_element(obj.content)}]"

To add a new writer, you have to add a new file in the `writers` folder, create a class with your writer, and add a proper import to the `__init__.py` file.
