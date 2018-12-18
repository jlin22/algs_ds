def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def bubble_down(array, i):
    ''' Bubble down in a min_heap '''
    # no children
    length = len(array)
    if 2 * i >= length:
        return 
    # left exists, but right doesn't
    elif 2 * i + 1 == length:
        # swap with the child if it is less than you
        if array[2 * i] < array[i]:
            swap(array, 2 * i, i)
        return
    # if both exist, swap with the minimum child
    else:
        minimum = (2 * i) if (array[2 * i] < array[2 * i + 1]) else (2 * i + 1)
        if array[minimum] < array[i]: 
            swap(array, minimum, i)
            return bubble_down(array, minimum)
        else:
            return

def extract_min(array, length):
    ''' Extract min of a min heap '''
    swap(array, 1, length - 1)
    minimum = array.pop()
    bubble_down(array, 1)
    return minimum

def heap_sort(array, debug=False):
    # create our heap
    n = len(array)
    array.insert(0, 0)
    for i in reversed(range(1, n // 2 + 1)):
        bubble_down(array, i)

    # create our sorted array by extract_max
    s = []
    for i in range(n):
        s.append(extract_min(array, len(array)))

    return s

array = [1, 45, 90, 66, 64, 43, 23, 12]
sorted_array = heap_sort(array)
print(array)
print(sorted_array)

array2 = [1, 45, 90, 66, 64, 43, 23, 12, 55]
heap_sort(array2)
print(array2)
print(sorted_array)
