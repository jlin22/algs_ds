class Node:
    left = None
    right = None
    parent = None     

    def __init__(self, value):
        self.value = value

def insert_helper(node, prev, key):
    if node == None: 
        if key < prev.value:
            prev.left = Node(key)
        else:
            prev.right = Node(key)
    else:
        if key < node.value:
            insert_helper(node.left, node, key)
        else:
            insert_helper(node.right, node, key)
    
def inorder_helper(node):
    if node != None:
        inorder_helper(node.left)
        print(node.value)
        inorder_helper(node.right)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            insert_helper(self.root, None, value)

    def inorder(self):
        inorder_helper(self.root)

bst = BinarySearchTree()
for i in range(10):
    bst.insert(i)
bst.insert(-1)
bst.insert(-3)
bst.inorder()
