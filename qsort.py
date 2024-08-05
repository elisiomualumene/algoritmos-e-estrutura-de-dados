import math

def qsort(arr):
    if len(arr) < 2:
        return arr
    
    tamanho = len(arr) - 1
    meio = math.ceil(tamanho/2)
    pivo = arr[meio] 
    menores = []
    maiores = []
    for x in arr[1:]:
        if x < pivo:
            menores.append(x)
        else:
            maiores.append(x)
            
    return qsort(menores) + [pivo] + qsort(maiores)

print(qsort([2, 5, 8, 3, 8, 9, 3]))


""" Caso Base """