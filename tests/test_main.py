import pytest
from main import crawl_schema, get_type


def test_get_types():
    test_attr_1 = ["cat", "bat", "sat"]
    test_attr_2 = [
        {
            "name": "John",
            "age": 13
        }
    ]

    assert get_type(23) == "integer"
    assert get_type("Hello") == "string"
    assert get_type(test_attr_1) == "enum"
    assert get_type(test_attr_2) == "array"

    with pytest.raises(AttributeError):
        get_type(34.5)

    with pytest.raises(AttributeError):
        get_type(3+5j)

    with pytest.raises(AttributeError):
        get_type(("a", "b", "c"))
    
def test_crawl_schema():
    test_message_1 = {
        "name": ["a", "b"],
        "age": 13
    }
    test_schema_1 = {}
    crawl_schema(test_message_1, test_schema_1)

    result_1 = {
        "name": {
            "type": "enum",
            "tag": "",
            "description": "",
            "required": False,
        },
        "age": {
            "type": "integer",
            "tag": "",
            "description": "",
            "required": False,
        }
    }
    assert test_schema_1 == result_1
