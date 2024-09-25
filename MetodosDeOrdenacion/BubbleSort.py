import random

def bubbleSort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(n-i-1):
            #Intercambio si el elemento acutal es mayor que la posicion siguiente
            if(lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista

def glista(tam):
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
lista1 = glista(10)
print("Lista generada: ", lista1)

lista2 = bubbleSort(lista1)

print("\nLista 1: ")
print(lista1)

print("\nLista 2:")
print(lista1)

