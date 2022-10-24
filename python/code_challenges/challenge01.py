


class LinkedList:

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
                # print(current.value)
                nodes.append(current.value)
                current = current.next
        
        return nodes  

                
        
    def delete_node(self,node):
       # function that receive node and delete it
        prev = Node(node)
        # list1=[]
        if(node == None):
            return
        else:
            while(node.next != None):
                node.value = node.next.value
                prev = node
                node = node.next
  
            prev.next = None
       

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None




if __name__ == "__main__":
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)

    node2 = Node(12)
    linkedList1.append(node2)

    node3 = Node(7)
    linkedList1.append(node3)

    node4 = Node(3)
    linkedList1.append(node4)

    linkedList1.print_node()
    print('list after deleting:7 ')
    linkedList1.delete_node(node2)
    print('list after deleting: ')
    linkedList1.print_node()

