# FOR I, IF J > J+1, SWAP

def sort(arr):
    n = len(arr)
    
    for i in range(n):
        
        for j in range(0,n - 1):
        
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr


print(sort([5,4,3,2,1]))

# TROCAS
# 5, 4
# 5, 3
# 5, 2
# 5, 1
# 4, 3
# 4, 2
# 4, 1
# 3, 2
# 3, 1
# 2, 1