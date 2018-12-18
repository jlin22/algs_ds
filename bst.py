class Node:
    # a node in a BinarySearchTree
    left = None
    right = None

    def __init__(self, value):
        self.value = value

def insert_helper(node, prev, key):
    # recursive function that inserts key into the BST
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
    # inorder printing of the BST
    if node != None:
        inorder_helper(node.left)
        print(node.value)
        inorder_helper(node.right)

def inorder_save(node, stack):
    # creates a sorted array of the elements of the tree w/ root=node
    if node != None:
        inorder_save(node.left, stack)
        stack.append(node.value)
        inorder_save(node.right, stack)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # insert an element into the BST
        if self.root == None:
            self.root = Node(value)
        else:
            insert_helper(self.root, None, value)

    def inorder(self):
        # create a list of the elements in the BST in order
        stack = []
        inorder_save(self.root, stack)
        return stack

bst = BinarySearchTree()
for i in range(10):
    bst.insert(i)
bst.insert(-1)
bst.insert(-3)
print(bst.inorder())
