import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __eq__(self, other):
        return other != None and self.value == other.value
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, element):
        if not self.head: self.head = element
        else: 
            element.next = self.head
            self.head = element

    def delete(self, element):
        ''' Given a Node element, find it and delete it '''
        if not self.head: return None

        # initialize pointers to iterate through the ll
        prev = None
        current = self.head

        # try to find it
        while (current and current != element):
            prev = current
            current = current.next

        # either it doesn't exist, it's the first element, or its in the mid
        if current == None: return None
        elif prev == None: self.head = self.head.next
        else: prev.next = prev.next.next

        return element

    def search(self, key):
        current = self.head
        while (current):
            if current.value == key: return current
            else: current = current.next
        return None 

    def max(self):
        if not self.head: return None
        else:
            max_node = self.head
            current = self.head.next
            while (current):
                if current.value > max_node.value:
                    max_node = current
                current = current.next
        return max_node

    def min(self):
        if not self.head: return None
        else:
            min_node = self.head
            current = self.head.next
            while current:
                if current.value < min_node.value: min_node = current
                current = current.next
        return min_node

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __eq__(self, other):
        return other is not None and self.value == other.value

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def insert(self, node):
        if not self.head: self.head = node
        else: 
            self.head.prev = node
            node.next = self.head
            self.head = node

    def __str__(self):
        s = ''
        current = self.head
        while (current):
            s += str(current.value)
            if current.next:
                s += '->'
            current = current.next
        return s
            
    def delete(self, element):
        if not self.head: return None
        # assume element is a part of the list 
        element.prev.next = element.next # previous forgets element
        element.next.prev = element.prev # next forgets element
        # so nobody remembers element

    def max(self):
        if not self.head: return None
        max_node = self.head
        current = self.head.next
        while current:
            if current.value > max_node.value:
                max_node = current
            current = current.next
        return max_node

        
if __name__ == '__main__':
    ll = SinglyLinkedList()
    for i in range(0, 11, 2):
        ll.insert(Node(i))
    print(ll.delete(Node(5)))
    print(ll.search(5))
    print(ll.search(6).value)
    print(ll.max().value)
    print(ll.min().value)


    def swap(array, i, j):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

    ll = DoublyLinkedList()
    r = [55, 76, 15, 88, 75, 30, 79, 50, 66, 86]
    for value in r:
        ll.insert(DoubleNode(value))
    print(ll)
    ll.delete(ll.max())
    print(ll)

