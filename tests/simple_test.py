from markup_converter.simple_class import SimpleClass


def test_simple_class():
    simple_class = SimpleClass("test")
    assert str(simple_class) == "SimpleClass: test"
