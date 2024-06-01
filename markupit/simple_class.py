class SimpleClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"SimpleClass: {self.name}"


if __name__ == "__main__":
    simple_class = SimpleClass("test")
    print(simple_class)
