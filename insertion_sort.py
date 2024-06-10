# SWAP TO LEFT

def sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

print(sort([5,4,3,2,1]))

# PROGRESSO
# [4, 5, 3, 2, 1]
# [3, 4, 5, 2, 1]
# [2, 3, 4, 5, 1]
# [1, 2, 3, 4, 5]