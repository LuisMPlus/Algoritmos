import random
def insertionSort(lista):
    n = len(lista)
    for i in range(1, n):
        # Guardamos el valor actual que queremos ordenar
        key = lista[i]
        j = i - 1
        # Desplazamos los elementos mayores hacia adelante
        while (j >= 0 and lista[j] > key):
            lista[j + 1] = lista[j]  # Mueve el elemento hacia adelante
            j -= 1
        # Insertamos el valor en su posición correcta
        lista[j + 1] = key


def gLista(tam):
    lista = []
    r = 0
    for i in range(tam):
        r = random.randint(0, 101)
        lista.append(r)
    return lista
def estaOrdenada(lista):
    if (lista == sorted(lista)):
        print("La lista esta perfectamente ordenada")
    else:
        print("La lista NO esta ordenada--------------------------------------------------------------------------------------")



#PRINCIPAL
lista1 = gLista(10)
print("Lista generada: ", lista1)

insertionSort(lista1)
print("\nLista ordenada: ", lista1)

estaOrdenada(lista1)



""" 
def insertionSort(lst):
    for step in range(1, len(lst)):
        key = lst[step]
        j = step - 1      
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = key
    return lst
 """
