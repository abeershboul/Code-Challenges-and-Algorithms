# Write your test here
import pytest
from challenge01tree import TreeNode,build_Tree,printpreorder,printinorder,Breadth_first

def test_one():
   preorder= [-1]
   inorder=[-1]
   root =build_Tree(preorder,inorder)
    #actual = 
    #expected=
   assert printpreorder([],root)==[-1]

def test_tow():
   preorder= [3,9,20,15,7]
   inorder=[9,3,15,20,7]
   root =build_Tree(preorder,inorder)
   assert printpreorder([],root)==[3,9,20,15,7]
def test_three():
   preorder= [3,9,20,15,7]
   inorder=[9,3,15,20,7]
   root =build_Tree(preorder,inorder)
   assert printinorder([],root)==[9,3,15,20,7]

def test_four():
   preorder= [3,9,20,15,7]
   inorder=[9,3,15,20,7]
   root =build_Tree(preorder,inorder)
    
   assert Breadth_first([],root)==[3,9,20,15,7]      

