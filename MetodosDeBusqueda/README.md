# Search Algorithms
Estos devuelven el indice de la lista del elemento buscado si es que se encuentran, sino devuelven -1.

## 1. Linear Search
Trata basicamente de ir recorriendo la lista hasta que se halle el elemento buscado simplemente
Hay Cuatro formas de recorrer una lista en python.
### For each
<pre>
    for item in lista:
        if item == k:
            pos=i
        i +=1
</pre>
Va tomando cada elemento(no indice) de la lista a medida que la va iterando. Usamos la variable i para ubicar el indice del elemento.

### Range
<pre>
    for i in range(len(lista)):
        if lista[i] == k:
            pos=i
            break
</pre>
Simplemente la recorre usando a i de iterador.

### Enumerate
<pre>
    for i,item in enumerate(lista):
        if item == k:
            pos=i
            break
</pre>
Caso similar al for each solo que ademas de tomar el elemento tambien se toma su indice.

### While
<pre>
    while i < len(lista) and pos == -1:
        if lista[i] == k:
            pos=i
        else:
            i +=1
</pre>
Va iterando segun la condicion del while usando la variable i como iterador.

## 2. Binary Search
Algoritmo eficiente para la busqueda de un elemento.
Precondicion importante: La lista debe estar ordenada. Esto es por lo que lo vuelve eficiente
Cuestion que va jugando con los apuntadores de izquierda y derecha(son indices) mas una variable ***medio*** que ira marcando la division entera de la suma de izq y derecha. El fin de estas variables es ir acortando de mitad en mitad la busqueda del elemento de la lista.

<pre>
    izq = 0 
    der = len(lista) -1
</pre>

Se inicializa ***izq*** y ***der*** con los indices extremos de la lista

<pre>
    while izq <= der:
        medio = (izq+der)//2
        
        if lista[medio] == x:
            return medio
        elif lista[medio] > x:
            der = medio-1
        else:
            izq = medio+1
</pre>
En un while de mientras que izq sea menor o igal a der se prosigue a asignar a medio la division entera de 2 de la suma de los apuntadores.
En la parte de condicionales evalua primeramente si el elemento esta en la posicion medio, si es asi retorna el indice del medio.
En el segundo condicional evalua si en posicion medio es mayor al elemento, en caso que lo sea se procede con la asignacion de der, con el fin de ir acortando la lista.
Y si no ocurre ninguno de los anteriores entonces se procede con la asingacion de izq.
Si al terminar el while aun no retorno la posicion significa que no se encuentra en la lista y devueleve -1

