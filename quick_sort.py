# https://youtu.be/Vtckgz38QHs?si=7JcB0muGVpRRsfsX

def partition(array, low, high):
 
    # último elemento como pivô
    pivot = array[high]
 
    # mínimo elemento
    i = low - 1
 
    # iterar todos os elementos
    # comparando-os com pivô
    for j in range(low, high):
        if array[j] <= pivot:
 
            # se encontrar um elemento menor que o pivô
            # trocar com um menor apontado por i
            i = i + 1
 
            # trocando elemento i com j
            (array[i], array[j]) = (array[j], array[i])
 
    # trocar o pivô com o menor apontado por i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # retorna posição da repartição
    return i + 1
 
 
def quickSort(array, low, high):
    if low < high:
        # achar o pivô
        # elementos menores à esquerda
        # elementos maiores à direita
        pi = partition(array, low, high)
        print(array)

        # Direita
        quickSort(array, low, pi - 1)
 
        # Esquerda
        quickSort(array, pi + 1, high)
 
 
input = [5,4,3,2,1]
 
size = len(input)
 
print(quickSort(input, 0, size - 1))
 
# REPARTIÇÕES
# [1, 4, 3, 2, 5]
# [1, 4, 3, 2, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]