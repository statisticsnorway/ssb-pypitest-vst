from ssb_pypitest_vst.functions import example_function
from ssb_pypitest_vst.functions import print_hello_world


def test_example_function() -> None:
    assert example_function(1, 2) == "1 is less than 2"
    assert example_function(1, 0) == "1 is greater than or equal to 0"


def test_print_hello_world() -> None:
    assert print_hello_world("Alice") == "Hello Alice. Your function works!"
    assert print_hello_world("Bob") == "Hello Bob. Your function works!"
    assert print_hello_world("") == "Hello . Your function works!"  # edge case
