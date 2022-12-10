# Write your test here
import pytest
from challengehash01 import Target,Tree

def test_sum_bst():
    tree1=Tree(7)
    tree1.left=Tree(2)
    tree1.right=Tree(7)
    actual= Target(tree1,9)
    extcepted=True
    assert actual == extcepted

def test_sum_bst_tow():
    tree1=Tree(4)
    tree1.left=Tree(1)
    tree1.right=Tree(7)
    tree1.right.left=Tree(5)

    actual= Target(tree1,17)
    extcepted=False
    assert actual == extcepted    
