# https://www.youtube.com/watch?v=7zuGmKfUt7s&ab_channel=GeeksforGeeks

def countSort(arr):
    max_num = max(arr)
    output = [0 for _ in range(max_num + 1)]
    count = [0 for _ in range(max_num + 1)]
    ans = [0 for _ in arr]

    # Contar ocorrências
    for i in arr:
        count[i] += 1

    # Adicionar anterior com sucessor 
    for i in range(1, max_num + 1):
        count[i] += count[i-1]

    # Adiciona os elementos no espaço correspondender
    # E subtrai count por um
    for i in range(len(arr)):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

 
# Driver program to test above function
arr = [5,4,3,2,1]
print(countSort(arr))