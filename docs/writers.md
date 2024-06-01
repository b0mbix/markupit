# How writers work?
In our program we use writers to export structure written in Python to markup file. All of the writers are stored in file ``writers``.

There is an abstract class defining basic way a writer work. In this class there are following core functions:
- ``write`` - converts a document into string with content of markup file
- ``write_file`` - converts a document and writes it into markup file
- ``convert_element`` - finds and performs a converting action for an Element or an array of Elements

This is the core of every writer and generally it should not be changed.

Based on this core we can create our custom writers. The only thing we have to do is to write a proper text representation of each element. For instance, this is ``convert_strong`` function in ``TypstWriter``:
```py
    def convert_strong(self, obj: st.Inline.Strong) -> str:
        return f"#strong[{self.convert_element(obj.content)}]"
```


To add a new writer, you have to add new file in ``writers`` folder, create class with your writer, and add proper import to ``__init__.py`` file.
