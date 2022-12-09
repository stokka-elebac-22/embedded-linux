# test_capitalize.py
import pytest
from can_socket_server.python_script import capital_case
from hypothesis import given
from hypothesis import strategies as some

@pytest.mark.parametrize(
    ["word", "expected"], 
    [
        ("semaphore", "Semaphore"),
        ("test", "Test"),
        ("ehnei", "Ehnei"),
    ]
)
def test_capital_case(word: str, expected: str):
    result = capital_case(word)
    assert result == expected

@pytest.mark.parametrize(
    ["word", "error"], 
    [
        (5, AttributeError),
    ]
)
def test_capital_case_hypothesis(word: str, error: Exception):
    with pytest.raises(error):
        _ = capital_case(word)

@given(word = some.text())
def test_capital_case(word: str):
    result = capital_case(word)
    assert result == word.capitalize()
