import random

def selectionSort(lista):
    
    for i in range(len(lista)-1):
        min_index = i
        for j in range(i+1, len(lista)):
            
            if(lista[j] < lista[min_index]):
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista
        
    


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




#Principal
lista1 = gLista(10)
print("Lista generada: ", lista1)

selectionSort(lista1)
print("\nLista ordenada: ", lista1)

estaOrdenada(lista1)

