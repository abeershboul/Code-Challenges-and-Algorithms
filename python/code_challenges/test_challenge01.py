import pytest

from challenge01 import LinkedList,Node
nod1=Node(1)
nod2=Node(12)
nod3=Node(17)

test2=LinkedList()
test2.append(nod2)
test2.append(nod1)
test2.append(nod3)



def test_append2(): 
    
    actual = test2.print_node()
    expected=[12,1,17]
    assert actual ==expected



def test_delete_node():
    test2.delete_node(nod1)
    actual=test2.print_node()
    expected=[12,17]
    assert actual==expected
 

