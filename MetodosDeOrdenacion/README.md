# Sorting algorithms
## Considerations

### 1. Bubble Sort
Este algoritmo consiste en ir iterando la lista e ir comparando los elementos adyancentes para luego intercambiarlos, si es que fuera necesario, las veces que sean necesarias (por lo general hasta la longitud de la lista)
* Se compone principalemente de dos bucles for anidados. Bucle 1(el principal, en referencia que es el que incluye todo el dodigo hasta el return) y un bucle 2

*  El bucle 1 itera hasta la longitud de la lista<br>
<code>  for i in range(len(lista))</code>

* El bucle 2 itera hasta(len(lista)-i-1) 
**i** es el iterador del bucle 1 y hacer que reste es por cuestion de eficiencia pues cada vez que itera van quedando lo que son los valores mayores al final de la lista. El **-1** es por la condicion que estara dentro del bucle 2 <br>
<code>  for j in range(len(lista)-i-1)</code>

* Condicion que esta dentro del bucle 2 evalua si la posicion actual(**j** que es el iterador del bucle 2) es mayor que la posicion siguiente(iterador del bucle 2 + 1).<br>
<code>  if(lista[j] > lista[j+1]) </code><br>
En caso que se cumpla se hara un intercambio de valores de las posiciones <br>
<code>  lista[j], lista[j+1] = lista[j+1], lista[j]</code>

### 2. Insertion Sort
* Se compone de dos bucles anidados. El bucle 1 es un for y el bucle 2 es un while.

* El bucle 1 itera desde 1(incluido) hasta la longitud de la lista(excluido). Pues se considera que al haber un solo elemento en una 'sublista' ya esta ordenado. Consideramos la sublista al conjunto de los elementos anteriores respecto a lo que va iterando el bucle 1 <br>
<code>  for i in range(1, n):</code>

* Declaramos key la cual le asignamos la posicion **i**(iterador del bucle 1) de la lista <br>
<code>  key = lista[i]</code>

* Declaramos **j**, a la cual le asignamos **i** menos 1. Que correspondría inicialmente a la posicion anterior de la lista respecto al bucle 1 <br>
<code>  j = i - 1</code>

*  El bucle 2 itera mientras se cumpla la siguiente condicion: <br>
1. Que **j** sea mayor o igual a 0. Para que no quede en un bucle infinito. <br>
2. Y que la lista en una posicion **j** sea mayor a la key declarada y definida anteriormente. Subcondicion para ir posicionando a la key de forma que quede ordenado. <br>
Con el objetivo de ir ordenando la sublista. A medida que itera el bucle 1 se añade un elemento en la sublista a ser correctamente odernada por el bucle 2 <br>
<code>  while(j >= 0 and lista[j] > key)</code>

* En la posicion **j+1** de la lista se le asigna la posicion **j** de la lista <br>
<code>  lista[j + 1] = lista[j]</code>

* Se le decrementa j en 1. Para que siga iterando respecto a la condicion del while <br>
<code>  j -= 1</code>

* Al terminar el bucle 2 posicionamos la key en **j+1** de la lista <br>
<code>  lista[j + 1] = key</code>

### 3. Selection Sort
Este algoritmo consiste en ir iterando la lista e ir agarrado la posicion del valor minimo de la lista e intercambiarlo con los primeros elementos de la lista.
* Se compone en cuestion de codigo en dos bucles anidados

* Bucle 1 desde 0 hasta la longitud de la lista menos 1<br>
<code>  for i in range(len(lista)-1):</code>

* Se declara una variable que correspondría al indice del elemento que sea el menor de la lista y se inicializa en el iterador del bucle 1.<br>
<code>  indMIn = i</code>

* Luego en el bucle 2(for) se reccorre la lista con el objetivo de encontrar el indice del menor valor de la lista, el cual se guarda en la variable declarada anteriormente <br>
<pre>  for j in range(i+1, len(lista)):
    if(lista[j] lista[indMIn]):
        indMIn = j</pre>

* Al terminar el bucle 2 se procede a intercambiar de los primeros elementos con los valores minimos encontrados de la lista <br>
<code>  lista[i], lista[indMIn] = lista[indMIn], lista[i]</code>

### 4. Merge Sort




### 5. Shell Sort
Se compone de tres bucles(dos while y un for). En vez de ir comparando elementos adyacentes como algunos algoritmos anteriores en este se comparan a una cierta distancia que estara determinada con lo que llamaremos gap. 
* Se incializa el gap en la mitad entera de la longitud de la lista <br>
<code>  gap = n // 2 </code>

* Luego se procede con el bucle 1 que contiene al resto del codigo. Bucle el cual mientras el gap sea mayor a cero seguira ejecutandose, esto porque depues lo disminuimos. <br>
<code>  while gap > 0</code>

* Bluce 2 que recorre la lista desde el gap hasta la longitud de la lista. En la primera iteracion recorrera desde la mitad de la lista hasta el final de la misma depues esa distancia de mitad se ira reduciendo de mitad en mitad hasta que sea 0 <br>
<code>  for i in range(gap, len(lista))</code>

* Se declara una variable temporal a la cual se le asigna la posicion **i** del iterador del bucle 2 de la lista. Y **j** que inicializa con **i** <br>
<pre>   tmp = lista[i] 
    j = i</pre>

* Bucle 3 que mientras j sea mayor o igual al gap y lista en posicion **[j-gap]** sea mayor a la variable temporal se ejecutara el bucle <br>
<code>  while j >= gap and lista[j - gap] > tmp</code>

* Se asigna en lista posicion **j** el valor de la posicion **[j-gap]** y de decrementa **j** en menos **gap** <br>
<pre>   lista[j] = lista[j - gap]
    j -= gap</pre>

* Al terminar el bucle 3 se divide enteramente el gap en 2. Para la siguiente iteracion del bucle 2 <br>
<code>  gap = gap // 2 </code>

### 6. Quick Sort
Consiste en subdivir la lista en sublistas que se vayan ordenando mediante la recursion. Utiliza el paradigma divide y venceras 
* Primeramente la funcion recibe tres parametros tanto sean la lista, start y stop. <br>
<code>def quicksort(lista, start, stop)</code>

* 