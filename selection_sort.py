# SELECTION SORT
# MIN = i
# IF ANY < MIN: SWAP

def sort(list : list[any]):
    for i in range(len(list)):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list

print(sort([5,4,3,2,1]))

# [5, 4, 3, 2, 1], min_idx = 4, i = 0
# Troca o elemento na posição 0 (5) com o elemento mínimo (1)
# [1, 4, 3, 2, 5]

# [1, 4, 3, 2, 5], min_idx = 3, i = 1
# Troca o elemento na posição 1 (4) com o elemento mínimo (2)
# [1, 2, 3, 4, 5]

# [1, 2, 3, 4, 5], min_idx = 2, i = 2
# Não há troca, pois o elemento mínimo (3) já está na posição correta
# [1, 2, 3, 4, 5]

# [1, 2, 3, 4, 5], min_idx = 1, i = 3
# Não há troca, pois o elemento mínimo (4) já está na posição correta
# [1, 2, 3, 4, 5]

# [1, 2, 3, 4, 5], min_idx = 0, i = 4
# Não há troca, pois o elemento mínimo (5) já está na posição correta
# [1, 2, 3, 4, 5]

# Resultado final: [1, 2, 3, 4, 5]