from demo.foo import add
import pytest
def test_add():
    assert add(1, 2) == 3