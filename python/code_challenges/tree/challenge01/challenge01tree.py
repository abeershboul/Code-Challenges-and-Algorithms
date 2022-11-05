# Write here the code challenge solution


class TreeNode:
    '''
    A class that represents a binary tree 
    '''
    def __init__(self,value=0,left=None,right=None) :
        self.value=value
        self.left=left
        self.right=right

def build_Tree(prerder :list[int],inorder:list[int]):
        '''
    A function that takes two lists [preorder] and [inorder] as arguments 
    and return a root of the tree
        '''
    

        if not prerder or not inorder:
            return None
        if len(prerder)==1 and len(inorder)==1:
            root=TreeNode(prerder[0])
            
            return root
        mid = prerder.pop(0)
        root = TreeNode(mid)
        idx = inorder.index(mid)
        root.left = build_Tree(prerder, inorder[:idx])
        root.right = build_Tree(prerder, inorder[idx+1:])
         
        return root

def printpreorder(p,root):
    '''
    A function that takes a root node of tree and and list as arguments 
    and returns a list of the value of the nodes by follows pre_order algorithm    
    '''
    

   
    if root:
        p.append(root.value)
    if root.left:
        printpreorder(p,root.left)
    if root.right:
        printpreorder(p,root.right)
       
    return p

def printinorder(p,root):
    '''
    A function that takes a root node of tree and and list as arguments 
    and returns a list of the value of the nodes by follows inorder algorithm    
    '''
   
    if root.left:
        printinorder(p,root.left)
    if root:
        p.append(root.value)    
    if root.right:
        printinorder(p,root.right)
       
    return p


def Breadth_first(bf,root):    
     
    '''
    A function that takes a root node of tree and and list as arguments 
    and returns a list of the value of the nodes by follows Breadth first algorithm    
    '''
    if not root:
        bf.append(None)
        return
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        if current.left :
            queue.append(current.left)
        if current.right :
            queue.append(current.right)
        bf.append(current.value)
    return bf
    
preorder= [3,9,20,15,7]
inorder=[9,3,15,20,7]
root =build_Tree(preorder,inorder)   
print(Breadth_first([],root))