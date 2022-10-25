# Write your test here
import pytest
from challenge02 import LinkedList , Node

# nod1=Node(1)
# nod2=Node(12)
# nod3=Node(17)

# test2=LinkedList()
# test2.append(nod2)
# test2.append(nod1)
# test2.append(nod3)

@pytest.fixture
def creat():
    nod1=Node(1)
    nod2=Node(12)
    nod3=Node(17)

    test2=LinkedList()
    test2.append(nod2)
    test2.append(nod1)
    test2.append(nod3)
    return test2

def test_append(creat): 
    actual = creat.print_node()
    expected=[12,1,17]
    assert actual ==expected

    
def test_middleNode(creat):
 # length of linkedlist is odd

    actual=creat.result()
    expected=[1,17]
    assert actual==expected

def test_middleNode2(creat):
    # length of the linkedlist is even
   
    node5=Node(15)
    
    
    creat.append(node5)
   
    actual= creat.result()
    expected= [17,15]
    assert actual==expected

def test_middle_empty():
    linkedlist1=LinkedList()
    actual=linkedlist1.printMiddle()
    expected="the number of node inside linked List is less than one or more than 100"
    assert actual==expected
