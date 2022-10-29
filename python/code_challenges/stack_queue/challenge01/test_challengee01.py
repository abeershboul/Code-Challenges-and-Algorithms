# Write your test here
import pytest
from challengee01 import Stack,MyQueue,Node
@pytest.fixture
def creat ():
    queue=MyQueue()
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    return queue



def test_enqeue_value(creat):
    
    actual=creat.enqueue(8)
    expected=[4,5,6,7,8]
    assert actual==expected
    
def test_deqeue(creat):
    actual=creat.dequeue()
    expected=4
    assert actual==expected

def test_deqeue_2value(creat):
    creat.dequeue()
    actual=creat.dequeue()
    expected=5
    assert actual==expected

def test_peek(creat):
    
    actual=creat.peek()
    expected=4
    assert actual==expected

def test_is_empty(creat):
    
    actual=creat.is_empty_queue()
    expected=False
    assert actual==expected    

def test_is_empty2():
    queue2=MyQueue()
    
    actual=queue2.is_empty_queue()
    expected=True
    assert actual==expected     


