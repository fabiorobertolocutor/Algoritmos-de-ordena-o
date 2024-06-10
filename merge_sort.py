# https://youtu.be/3j0SWDX4AtU?si=YtoYuaJqBFKY_nx5&t=111

def sort(arr):
    # Caso base: se o tamanho da lista for menor ou igual a 1, ela já está ordenada
    if len(arr) <= 1:
        return arr
    
    # Dividir a lista em duas metades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursivamente ordenar as duas metades
    left_half = sort(left_half)
    right_half = sort(right_half)

    # Mesclar as duas metades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    
    # Comparar os elementos das duas metades e adicionar o menor à lista mesclada
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Adicionar os elementos restantes da metade que ainda possui elementos
    while i < len(left):
        merged.append(left[i])
        i += 1
        
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

print(sort([6, 5,4,3,2,1]))

# DIVISION
# left:[5] right:[4]
# left:[6] right:[4, 5]
# left:[2] right:[1]
# left:[3] right:[1, 2]
# left:[4, 5, 6] right:[1, 2, 3]