from time import sleep

def merge(array, aux, low, mid, high):
    aux[low: high+1] = array[low: high+1]
    i, j = low, mid+1
    k = low
    print(low, mid, high)
    while k <= high:
        if i > mid:
            array[k] = aux[j]
            j += 1
        elif j > high:
            array[k] = aux[i]
            i += 1
        elif aux[i] > aux[j]:
            array[k] = aux[j]
            j += 1
        else:
            array[k] = aux[i]
            i += 1
        k += 1

def merge_sort(array, aux, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(array, aux, low, mid)
        merge_sort(array, aux, mid + 1, high)
        merge(array, aux, low, mid, high)

def sort(array):
    aux = [0 for i in range(len(array))]
    merge_sort(array, aux, 0, len(array) - 1)
    return array

array = [1, 45, 90, 66, 64, 43, 23, 12, 55]
print(sort(array))

