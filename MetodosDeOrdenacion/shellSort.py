import random
# https://www.youtube.com/watch?v=qzXAVXddcPU
def shellSort(lista):
    n = len(lista)
    gap = n // 2 #inicialmente, el valor del gap es la mitad del tamaño de la lista. Este valor controla la distancia entre los elementos que se van a comparar y ordenar
    while gap > 0: # se recorre la lista y se reduce el gap al final de cada iteración, se ejecutan las instrucciones mientras que el gap sea mayor a 0
        for i in range(gap, n): #recorre la lista desde el indice gap hasta el final de la lista. En cada iteración se toma un elemento de la lista y se 
            #compara con elementos anteriores que estan a una distancia "gap" 
            tmp = lista[i] #se guarda el valor actual en una variable temporal
            j = i #se inicializa la variable j con el indice actual
            """ Mientras j sea mayor o igual a gap y el valor en lista[j - gap] (el elemento a gap posiciones atrás) 
            sea mayor que tmp, se "desplaza" el valor lista[j - gap] hacia la derecha (a la posición j).
            Se actualiza j restándole gap para comparar con el siguiente elemento a la izquierda (a una distancia de gap).
            Una vez que se encuentran los elementos correctos para el intercambio, se asigna tmp a la posición correcta en 
            la lista lista[j]. """
            while j >= gap and lista[j - gap] > tmp:
                print(lista)
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = tmp

        gap = gap // 2 
        """ Una vez que todos los elementos a la distancia gap han sido comparados, 
            se reduce el gap a la mitad (división entera) y el proceso se repite con un gap mas pequeño.
            Este proceso repite hasta que gap es igual a 1 """

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
