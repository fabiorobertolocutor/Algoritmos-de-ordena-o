# https://www.youtube.com/watch?v=mgUiY8CVDhU&ab_channel=AbhilasBiswas

def sort(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        sort(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        sort(arr, n, i)



    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        sort(arr, i, 0)

arr = [5,4,3,2,1]
heapSort(arr)
print(arr)
