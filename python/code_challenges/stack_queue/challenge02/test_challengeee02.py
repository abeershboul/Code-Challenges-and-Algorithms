import pytest
from challengeee02 import Valid_Parentheses


def test_valid():
    actual=Valid_Parentheses('"[{(())}]"')
    expected=True
    assert actual==expected
def test_valid2():
    actual= Valid_Parentheses("[(hello)()]")
    expected=True
    assert actual==expected
def test_invalid():
    actual=Valid_Parentheses('(JDD)[})')    
    expected=False
    assert actual==expected