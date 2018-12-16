class BinarySearchTree:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def search(self, key):
        if not self.value: return None
        if self.value == key: return self
        elif self.value < key: 
            if not self.right: return None
            return self.right.search(key)
        else:
            if not self.left: return None
            return self.left.search(key)

    def find_min(self):
        if not self.value: return None
        min_tree = self
        while min_tree.left:
            min_tree = min_tree.left
        return min_tree

    def find_max(self):
        if not self.value: return None
        max_tree = self
        while max_tree.right:
            max_tree = max_tree.right
        return max_tree

    def traverse_tree(self):
        if self:
            self.left.traverse_tree()
            print(self.value)
            self.right.traverse_tree()

    def insert(self, key):
        if not self.value: 
            self.value = key
            return
        elif key <= self.value:
            if not self.right:
                self.right = BinarySearchTree()
                self.right.value = key
                return
            else: self.right.insert(key)
        else:
            if not self.left:
                self.left = BinarySearchTree()
                self.left.value = key
                return
            else: self.left.insert(key)
        

bst = BinarySearchTree()
for i in range(10):
    bst.insert(i)
print(bst.search(5))
print(bst.find_min().value)
print(bst.find_max().value)
bst.traverse_tree()


        
