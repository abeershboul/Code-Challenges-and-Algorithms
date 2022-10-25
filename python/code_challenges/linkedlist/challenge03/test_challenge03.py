# Write your test here
import pytest
from challenge03 import LinkedList,Node

@pytest.fixture
def creat():
    nod1=Node(1)
    nod2=Node(12)
    nod3=Node(17)
    nod4=Node(6)
    nod5=Node(5)

    linkedlist1=LinkedList()
    linkedlist1.append(nod1)
    linkedlist1.append(nod2)
    linkedlist1.append(nod3)
    linkedlist1.append(nod4)
    linkedlist1.append(nod5)


    return linkedlist1

def test_remove_4th_node(creat):
    creat.remove_nth_value(4)
    actual=creat.print_node()
    expected=[1,17,6,5]   
    assert actual==expected 

def test_remove_2th_node(creat):
    creat.remove_nth_value(2)
    actual=creat.print_node()
    expected=[1,12,17,5]   
    assert actual==expected 

def test_remove_more_sizeof_node(creat):
    creat.remove_nth_value(8)
    actual=creat.print_node()
    expected=[1,12,17,6,5]   
    assert actual==expected    

def test_remove_head_node():
    linkedlist2=LinkedList()
    node=Node(2)
    linkedlist2.append(node)

    linkedlist2.remove_nth_value(1)
    actual=linkedlist2.print_node()
    expected=[]  
    assert actual==expected    
