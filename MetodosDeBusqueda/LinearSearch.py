def lineal01(lista,k):
    pos, i = -1, 0
    for item in lista:
        if item == k:
            pos=i
        i +=1
    return pos

def lineal02(lista,k):
    pos=-1
    for i in range(len(lista)):
        if lista[i] == k:
            pos=i
            break
    return lista[pos]

def lineal03(lista,k):
    pos = -1
    for i,item in enumerate(lista):
        if item == k:
            pos=i
            break
    return pos

def lineal04(lista,k):
    pos, i = -1, 0
    while i < len(lista) and pos == -1:
        if lista[i] == k:
            pos=i
        else:
            i +=1
    return pos