class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, key):
        new_head = Node(key)
        new_head.next = self.head
        self.head = new_head

    def pop(self):
        val = self.head.value
        self.head = self.head.next
        return val

    def search(self, key):
        current = self.head
        while (current):
            if current.value[0] == key:
                return current.value[1]
            current = current.next

        return None

    def delete(self, key):
        current = self.head
        prev = None
        while current:
            if current.value[0] == key:
                if not prev:
                    self.head = self.head.next
                    return current.value[1]
                else:
                    val = current.value[1]
                    prev.next = current.next
                    return val
            prev = current
            current = current.next
        return None

    def __str__(self):
        s = '['
        current = self.head
        while current:
            s += str(current.value)
            s += ', ' if (current.next) else ']'
            current = current.next
        return s

class HashTable:
    BASE_SIZE = 8

    def __init__(self):
        self.array = []
        self.size = self.BASE_SIZE
        for i in range(self.size):
            self.array.append(LinkedList())

    def hash(self, key, size):
        h = 0
        for c in key:
            h *= 256
            h += ord(c)
            h %= size
        return h

    def insert(self, key, value):
        if value == None:
            raise Exception('value cannot be None')
        ind = self.hash(key, self.size)
        (self.array[ind]).push((key, value))

    def search(self, key):
        ind = self.hash(key, self.size)
        return (self.array[ind]).search(key)
    
    def delete(self, key):
        ind = self.hash(key, self.size)
        return (self.array[ind]).delete(key)

    def __str__(self):
        s = ""
        for llist in self.array:
            s += str(llist)
        return s

'''
s = LinkedList()
for i in range(10):
    s.push(i)
print(s)
'''

ht = HashTable()
strs = ["hello", "world", "space", "cats", "dogs", "life", "chaos", "suffering", \
        "patience", "sucking", "overcome", "why", "first time"]
for i, string in enumerate(strs):
    ht.insert(string, i)
print(ht)
print('chaos', ht.search('chaos'))
print('space', ht.search('space'))
print('meaning', ht.search('meaning'))
print(ht.delete('chaos'))
print(ht.delete('hello'))
print(ht)
