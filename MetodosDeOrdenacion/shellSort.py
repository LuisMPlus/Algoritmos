import random
# https://www.youtube.com/watch?v=qzXAVXddcPU
def shellSort(lista):
    n = len(lista)
    gap = n // 2 
    while gap > 0:
        for i in range(gap, n): 
            tmp = lista[i] 
            j = i 

            while j >= gap and lista[j - gap] > tmp:
                print(lista)
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = tmp

        gap = gap // 2 

    return lista

def glista(tam):
    lista = []
    r = 0
    for i in range(tam):
        r = random.randint(0, 20)
        lista.append(r)
    return lista

# Ejemplo
lista = [12, 11, 13, 5, 6]
print("Lista desordenada:", lista)
listaOrdenada = shellSort(lista)
print("Lista ordenada:", listaOrdenada)
