# Write here the code challenge solution
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    '''
    class have 4 methoud :
        1- ineshlized method declare head virable
        2 - append methoud that receve node as primeter and add it to the linkedlist
        3 - print node methud that print the node value
        4- remove_nth_value that recive position of node that will be deleted as parmiter and the declear 2 pointer to loop throw linkedlist
        and delete  from the end of the list and return its head. 
        
    
    
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
                #print(current.value)
                nodes.append(current.value)
                current = current.next
            print(nodes)
        return nodes 

    def remove_nth_value(self,n):
        slow = self.head
        fast = self.head
        for i in range(n):
             
            # count of nodes in the list is less than 'n'
            if(fast.next == None):
                 
                if(i == n - 1):
                    self.head = self.head.next
                return self.head
            fast = fast.next
         
        while(fast.next != None):
            fast = fast.next
            slow = slow.next
         
        slow.next = slow.next.next
        



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
linkedList1.remove_nth_value(2)
linkedList1.print_node()                        




