# Write here the code challenge solution
class Node:
 
    # Construct to create a newNode
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def convert_arr_to_bst (arr):
    '''
     function to convert sorted array to a
     balanced BST
    
    '''

    if not arr:
        return None

    arr.sort()
    
    # index of the mid
    mid=(len(arr))//2
    #print(mid)
    root=Node(arr[mid])
    root.left=convert_arr_to_bst(arr[:mid])
    root.right=convert_arr_to_bst(arr[mid+1:])

    return root



def bridth_BT (root):
    '''
    function that print the tree in  breadth first traversal algoretham
    '''
    if root is None:
        return None
    list=[]    
    queue=[]
    queue.append(root)
    

    while len(queue)>0:
        print(queue[0].val,end=" ")
        s=queue[0].val
        list.append(s)
        node=queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return list





arr = [3,-9,5,7,2,5]
root = convert_arr_to_bst(arr)  
bridth_BT(root)
