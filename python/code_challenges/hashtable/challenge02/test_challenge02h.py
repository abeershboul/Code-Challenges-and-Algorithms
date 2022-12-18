# Write your test here
import pytest
from .challenge02hasht import repeated_Word

def test_Repeated_word1():
    actual= repeated_Word('wellcom to hashtable')
    expected= 'No Repetition'
    assert actual == expected

def test_Repeated_word2():
    actual= repeated_Word('hashtable wellcom to hashtable')
    expected= 'hashtable'
    assert actual == expected
     