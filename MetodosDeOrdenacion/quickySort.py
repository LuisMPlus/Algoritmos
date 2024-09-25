import random

""" La función quicksort recibe tres parámetros:
    lista: la lista de elementos a ordenar.
    start: el índice de inicio de la sublista que se está ordenando.
    stop: el índice final de la sublista que se está ordenando. """

# Animacion: https://www.youtube.com/shorts/t40PfJDPWkk?feature=share










def quicksort(lista, start, stop):
    print(lista)
    if stop - start > 0:
        pivot, left, right = lista[start], start, stop
        print("Pivot es  :", pivot)

        while left <= right:
            while lista[left] < pivot:
                left += 1
            while lista[right] > pivot:
                right -= 1
            if left <= right:
                lista[left], lista[right] = lista[right], lista[left]
                left += 1
                right -= 1

        print("Izquierda :", lista[start:right+1])
        quicksort(lista, start, right)
        print("Derecha   :", lista[left:stop+1])
        quicksort(lista, left, stop)
    return lista














def glista(tam):
    lista = []
    r = 0
    for i in range(tam):
        r = random.randint(0, 20)
        lista.append(r)
    return lista

# Ejemplo
""" lista = glista(10)
print("Lista desordenada:", lista)
listaOrdenada = quicksort(lista, 0, len(lista)-1)
print("Lista ordenada:", listaOrdenada) """


lista = [7, 4, 3, 5, 10, 1, 2]


listaOrdenada = quicksort(lista, 0, len(lista)-1)
print("Lista ordenada:", listaOrdenada)
