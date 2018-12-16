class Heap:
    ''' For heaps, implement extract min, min, insert '''

    def __init__(self, compare):
        ''' Initialize an array with the 0 index taken 
        and use compare for the data'''
        self.array = [0]
        self.index = 1

    @staticmethod
    def parent(n):
        return n // 2

    @staticmethod
    def left_child(n):
        return 2 * n

    @staticmethod
    def right_child(n):
        return 2 * n + 1

    @staticmethod
    def swap(array, p, q):
        temp = array[p]
        array[p] = array[q]
        array[q] = temp 

    def bubble_up(self, n):
        ''' A recursive method for bubbling up the nth element of the heap '''
        if n == 1: return # you're at the root and can't go higher
        elif compare(self.array[self.parent(n)], self.array[n]) > 0: 
            # the parent is less than the child
            self.swap(self.array, self.parent(n), n)
            self.bubble_up(self.parent(n))
        else:
            return

    def insert(self, key):
        ''' Insert the key into the heap ''' 
        # put it at the end and increment the index
        self.array.append(key)
        self.bubble_up(self.index)
        self.index += 1
        # now the heap may be violated, so we need to bubble it up

    def __repr__(self):
        return str(self.array)

    def bubble_down(self, n):
        left, right = self.left_child(n), self.right_child(n)
        if right > self.index:
            if left <= self.index and compare(self.array[n], self.array[left])\
                < 0: 
                self.swap(self.array, n, left_child)
                return
        if n >= self.index: return 
        # you dominate your children
        elif compare(self.array[n],self.array[left]) > 0 and \
        compare(self.array[n],self.array[right]) > 0: return
        else:
            max_child = left
            if right > left: max_child = right
            self.swap(self.array, n, max_child)
            self.bubble_down(max_child)

    def remove_max(self):
        if self.index == 1: return
        else:
            maximum = self.array[1]
            self.index -= 1
            self.array[1] = self.array[self.index]
            self.array.pop()
            self.bubble_down(1)

def compare(a, b):
    if a == b: return 0
    elif a < b: return -1
    else: return 1

heap = Heap(compare)
for i in reversed(range(10)):
    heap.insert(i)
print(heap)
for i in range(5):
    heap.remove_max()
heap.remove_max()
heap.remove_max()
print(heap)
heap.remove_max()
print(heap)
