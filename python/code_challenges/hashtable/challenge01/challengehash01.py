# Write here the code challenge solution
class Tree():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def Target(root,k):
    '''
      function that takes a Binary Search tree and an integer as a parameter. 
      Return True if Binary search tree has two elements that their summation is the given integer.
    '''
    values = []
    def Two_Sum_BST(node):
        if not node:
            return False
        y = k - node.val
        if y in values:
            return True
        else:
            values.append(node.val)
        return Two_Sum_BST(node.left) or Two_Sum_BST(node.right)
    
    return Two_Sum_BST(root)




tree1=Tree(7)
tree1.left=Tree(2)
tree1.right=Tree(7)
tree1.left.left=Tree(1)
tree1.left.right=Tree(5)
tree1.right.right=Tree(9)
print(tree1.val)
print(Target(tree1,3))
print(Target(tree1,4))


          


