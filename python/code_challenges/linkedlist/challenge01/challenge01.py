

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    
    '''
    Linked List class :Its class to create  a linked list with and it have 3 method
    1- __init__ methoud that inshlized head virable
    2- append mehoud to add new node to the linked list
    3- print_node method print to print all the node in the linked lis


    
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
            return "The linked list is empty"
        else:
            current = self.head
            while current is not None:
                # print(current.value)
                nodes.append(current.value)
                current = current.next
        
        return nodes  

                
        
    
       


def delete_node(node):
    '''
    methode delete to remove specific node 
    '''
    if node == None:
      return 
    else:
      if node.next == None:
        print("can't be remove tail")
        return
      node.value = node.next.value
      node.next = node.next.next


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

    print('linkedlist befor delete',linkedList1.print_node())

    print('--------------')
    delete_node(node3)
    print("list after deleting",linkedList1.print_node())

