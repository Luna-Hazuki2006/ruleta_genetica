import math
import itertools

def colisiones(lista : tuple[int], cantidad : int): 
    veces = 0
    for i, cada in enumerate(lista[:cantidad]): 
        positivo = True
        negativo = True
        sumas = cada + 1
        restas = cada - 1
        for j in range(i + 1, len(lista)): 
            if sumas == lista[j] and positivo: 
                veces += 2
                positivo = False
            if restas == lista[j] and negativo: 
                veces += 2
                negativo = False
            sumas += 1
            restas -= 1
    return veces

def combinar(cantidad : int = 4): 
    tableros = []
    lista = list(range(cantidad))
    # veces = math.factorial(cantidad) / (math.factorial(cantidad - 2) * math.factorial(2))
    for esto in list(itertools.permutations(lista, cantidad)): 
        if not tuple(reversed(esto)) in tableros: tableros.append(esto)
    for i in range(len(tableros)): 
        cuerpo = {'tabla': tableros[i]}
        cuerpo['colisiones'] = colisiones(tableros[i], cantidad)
        tableros[i] = cuerpo
    mejores = list(filter(lambda x: x['colisiones'] == 0, tableros))
    return mejores