# Write here the code challenge solution
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    '''
    class have 5 methoud :
        1- ineshlized method declare head virable
        2 - append methoud that receve node as primeter and add it to the linkedlist
        3 - print node methud that print the node value
        4 - get_len methoud that return the length or the linkedlist
        5 - printmiddle methoud return the middle node of the linked list
    
    
    '''

    def __init__(self):
        self.head = None

    def append(self, node):
        # function that receive node and add it

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node


        
        
    def print_node(self):

        nodes=[]
        if self.head is None:
            print("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                print(current.value)
                nodes.append(current.value)
                current = current.next
        
        return nodes 


    def getLen(self):
        temp = self.head
        len = 0
 
        while (temp != None):
            len += 1
            temp = temp.next
 
        return len

   


    def printMiddle(self):
        current=self.head
        count=0
        while True:
            if current==None:
                break
            else:
                count+=1
            current=current.next
        
        if count<1 or count>100:
            print('the number of node inside linked List is less than one or more than 100')
            return "the number of node inside linked List is less than one or more than 100"
        



        
        if self.head != None:
            # find length
            
            len = self.getLen()
            temp = self.head
 
            
            midIdx = len // 2
            while midIdx != 0:
                
                temp = temp.next

                midIdx -= 1
               
            print('The middle is ', temp.value)     
            
            return temp

            
    def result (self):
        mid_list=[]
        temp = self.printMiddle() 
        while temp.next is not None:
                mid_list.append(temp.value)
              #  print(temp.value)
                temp = temp.next
        mid_list.append(temp.value)    
                 
                
        print(mid_list) 
        return mid_list  
            
              

linkedList1 = LinkedList()
node1 = Node(1)
linkedList1.append(node1)

node2 = Node(12)
linkedList1.append(node2)

node3 = Node(7)
linkedList1.append(node3)

node4 = Node(3)
linkedList1.append(node4)
node5 = Node(9)
linkedList1.append(node5)
node6 = Node(6)
linkedList1.append(node6)
linkedList1.print_node()
print("------------------------")

linkedList1.printMiddle()  
linkedList1.result() 


        