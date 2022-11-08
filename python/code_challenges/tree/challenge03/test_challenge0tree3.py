# Write your test here
import pytest
from challenge03tree import Node, convert_arr_to_bst, bridth_BT

def test_first():
    arr=[0,-3,-10,5,9]
    root=convert_arr_to_bst(arr)
    actual=bridth_BT(root)
    expected=[0, -3, 9, -10, 5]
    assert actual==expected

def test_sucand():
    arr=[3,1]
    root=convert_arr_to_bst(arr)
    actual=bridth_BT(root)
    expected=[3,1]
    assert actual==expected 

def test_thared():
    arr=[3,-9,5,7,2,5]
    root=convert_arr_to_bst(arr)
    actual=bridth_BT(root)
    expected=[5,2,7,-9,3,5]
    assert actual==expected       
