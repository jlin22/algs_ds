class Node:
    # node for linked list
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, key):
        # push to the front of the linked list
        new_head = Node(key)
        new_head.next = self.head
        self.head = new_head

    def pop(self):
        # pop the first element of the linked list
        val = self.head.value
        self.head = self.head.next
        return val

    def search(self, key):
        # go through the linked list of tuples and try to find the key
        # if key is found, return val, else return None
        current = self.head
        while (current):
            if current.value[0] == key:
                return current.value[1]
            current = current.next

        return None

    def delete(self, key):
        ''' go through the linked list, delete the node with given key
        and return value associated w/ the key, else return None '''
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
        ''' list string representation'''
        s = '['
        current = self.head
        while current:
            s += str(current.value)
            if current.next:
                s += ', '
            current = current.next

        s += ']'
        return s

class HashTable:
    # make sure our hash table doesn't get smaller than this symbolic constant
    BASE_SIZE = 8

    def __init__(self):
        self.array = []
        self.size = self.BASE_SIZE
        self.elements = 0
        for i in range(self.size):
            self.array.append(LinkedList())

    def hash(self, key, size):
        ''' basic hash function for strings '''
        h = 0
        for c in key:
            h *= 256
            h += ord(c)
            h %= size
        return h

    def resized_array(self, size):
        # create a new array of linked lists of size
        array = []
        for i in range(size):
            array.append(LinkedList())
        return array

    def rehash(self, new_array, new_size):
        # rehash the elements in size.array with new hash function
        # put those elements in new_array
        
        # iterate through all of the linked lists
        for i in range(self.size):
            llist = self.array[i]

            # iterate through all of the elements in the linked lists
            current = llist.head
            while current:
                # rehash
                h = self.hash(current.value[0], new_size)
                # put the (key,value) onto the linked list at new[h]
                (new_array[h]).push(current.value)

                current = current.next

    def resize(self):
        ''' If self.elements / self.size >= 1 (load factor),
        then you want to double the size of it 
        if load factor == 0.25, then shrink it by half
        in both cases, rehash all of the elements'''
        load_factor = float(self.elements) / self.size
        if load_factor >= 1:
            new_array = self.resized_array(2 * self.size)
            self.rehash(new_array, 2 * self.size)
            self.array = new_array
            self.size *= 2
        elif load_factor <= 0.25:
            new_array = self.resized_array(self.size // 2)
            self.rehash(new_array, self.size // 2)
            self.array = new_array
            self.size = self.size // 2

    def insert(self, key, value):
        ''' insert key, val pair into our chained hash table '''
        if value == None:
            raise Exception('value cannot be None')
        ind = self.hash(key, self.size)
        (self.array[ind]).push((key, value))

        self.elements += 1
        self.resize()

    def search(self, key):
        ''' search for the key, returns val if found, None if not found '''
        ind = self.hash(key, self.size)
        return (self.array[ind]).search(key)
    
    def delete(self, key):
        ''' deletes key and returns value if it exists, else returns None
        and doesn't do anything '''
        ind = self.hash(key, self.size)
        val = (self.array[ind]).delete(key)
        if val:
            self.elements -= 1
        return val

    def __str__(self):
        s = "{"
        for i, llist in enumerate(self.array):
            s += str(llist)
            if i != len(self.array) - 1:
                s += ', '
        s += '}'
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
