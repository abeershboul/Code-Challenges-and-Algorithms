# Write here the code challenge solution
from inspect import stack


class Node:
    def __init__(self,value):
        self.next = None
        self.value =value


class Stack:
# Constructor
    def __init__(self):
        self.top = None
        self.size = 0
        self.list=[]

    def push(self,value):
        '''
        methoud that add item to the top of stack
        '''
        
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1
        self.list.append(value)
        return self.list

    def pop(self):       
        '''
        methoud that delete item from top of stack
        '''
       
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            self.list.pop()
            return temp.value
        else:
            return("This stack is empty")
    
    def peek(self):
        '''
        return item from top of stack
        '''
        if self.top:
            return self.top.value
        else:
            return("This stack is empty")

    def is_empty(self):
        '''
        method that check if the stack empty
        '''
        return self.size == 0

    def get_size(self):
        '''
        method that check the length of the stack
        '''
        return self.size

class MyQueue:
    def __init__(self):
       self.inputqueue=Stack()
       self.outputqueue=Stack()

    def enqueue (self,value):
       

        '''
       methoud that Move all elements from the first stack to the second stack
       and Add an item to the queue
       thenMove all elements back to the first stack 

        '''
        while not self.inputqueue:
            p=self.inputqueue.pop()
            self.outputqueue.push(p)
        ll=self.inputqueue.push(value)
        # return all elemant back to inputqueue
        while not self.outputqueue:
            pop_value=self.outputqueue.pop()
            self.inputqueue.push(value)
        return ll
           

    def dequeue (self):
        '''
        mehoud that Remove an item from the queue
        '''
        if self.outputqueue.is_empty() :

            while not self.inputqueue.is_empty():
                poped=self.inputqueue.pop()
                self.outputqueue.push(poped)
            
            poped_value=self.outputqueue.pop()  
        else:
            poped_value=self.outputqueue.pop() 

        #print(poped_value)
        return poped_value

    def is_empty_queue(self):
        '''
        method that check if the queue is empty
        '''
        return(self.inputqueue.is_empty() and self.outputqueue.is_empty())
    def peek(self):
        '''
        methoud that return the first elemant in the queue WITHOUT REMOVING IT
        '''
        if self.outputqueue.is_empty() :
            
              while not self.inputqueue.is_empty():
                poped=self.inputqueue.pop()
                self.outputqueue.push(poped)
              peek_value=self.outputqueue.peek()    
        else:
                peek_value=self.outputqueue.peek()

        return peek_value


if __name__ == '__main__':   
    q1=MyQueue()
    q2=MyQueue()
    #q2.enqueue('A')
    q1.enqueue(4)
    q1.enqueue(5)
    print(q1.enqueue(6))
    print(q1.enqueue(12))
    #q1.dequeue()
    print(q1.dequeue())
    print(q1.dequeue())

    #print(q1.peek())
    #q2.dequeue()
    # print(q2.peek())
    # print(q2.is_empty_queue())

        




            


                     
