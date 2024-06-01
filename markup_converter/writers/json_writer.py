import json

from markup_converter.structure.document import Document


class JsonWriter:
    """A class representing a JSON writer for a document.

    :param input: The document to write.
    :type input: Document
    """

    def __init__(self, input: Document) -> None:
        self.doc = input

    def write(self) -> dict:
        """Return a JSON representation of AST.

        :return: The document as a dictionary.
        """
        return self.doc.to_json()

    def write_to_file(self, filename: str) -> None:
        """Write the JSON representation of AST to a file.

        :param filename: The name of the file to write to.
        :type filename: str
        """
        with open(filename, "w") as file:
            json.dump(self.doc.to_json(), file)
