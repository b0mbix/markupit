from markup_converter.structure.document import Document
import json


class JsonWriter:
    def __init__(self, input: Document) -> None:
        self.doc = input

    def write(self) -> dict:
        return self.doc.to_json()

    def write_to_file(self, filename: str) -> None:
        with open(filename, "w") as file:
            json.dump(self.doc.to_json(), file)
