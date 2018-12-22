def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def selection(a):
    for i in range(len(a)):
        min_ind = i
        for j in range(i+1, len(a)):
            if a[min_ind] > a[j]:
                min_ind = j
        swap(a, i, min_ind)
    return a

a = [1, 5, 64, 12, 7]
print(selection(a))
            

