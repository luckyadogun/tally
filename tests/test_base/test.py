import pytest

def add(n):
    return n + 2


def test_add():
    assert add(2) == 4