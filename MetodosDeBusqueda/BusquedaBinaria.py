#IMPORTANTE. La lista debe estar previamente ordenada.

def busquedaBinaria(lista, x):
    """ Búsqueda Binaria 
    Precondición: lista está ordenada 
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] = x, si x está en lista
    """

    izq = 0 # izq guarda el índice inicio del segmento
    der = len(lista) -1 # der guarda el índice fin del segmento
    
    # un segmento es vacío cuando izq > der:
    while izq <= der:
        print(lista[izq:der])
        medio = (izq+der)//2
        if lista[medio] == x:
            return medio
        elif lista[medio] > x:
            der = medio-1
        else:
            izq = medio+1
    return -1


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pos = busquedaBinaria(lista, 6)

if(pos != -1):
    print(lista[pos])
else: 
    print("El elemento no se encuentra en la lista")



#Debugging
"""
Continue    Avanze al siguiente breakpoint
Step Over   Sigue al siguiente paso. A la siguiente linea del la parte principal del programa. No ingresa al metodo.
Step Into   Aca si ingresa al metodo
Step Out    Sale del metodo
Restart     Reinicar la ejecucion del codigo
Stop        Para toda la ejecucion
"""