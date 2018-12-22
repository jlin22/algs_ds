def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def insertion_sort(array):
    for i in range(len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j - 1, j)
            j -= 1
    return array

array = [1, 45, 90, 66, 64, 43, 23, 12]
array = insertion_sort(array)
print(array)
