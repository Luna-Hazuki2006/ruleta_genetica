import math
import itertools
from pprint import pprint
from colisiones import colisiones

def combinar(cantidad : int = 4): 
    tableros = []
    lista = list(range(cantidad))
    veces = math.factorial(cantidad) / (math.factorial(cantidad - 2) * math.factorial(cantidad))
    # veces = cantidad ** 2
    todos = list(itertools.permutations(lista, cantidad))
    pprint(len(todos))
    pprint(todos)
    print(veces)
    for i, esto in enumerate(todos): 
        # if not tuple(reversed(esto)) in tableros: tableros.append(esto)
        if i == veces / 2: break
        choques = colisiones(esto, cantidad)
        if choques != 0: continue
        cuerpo = {'tabla': esto, 'colisiones': choques}
        tableros.append(cuerpo)
    # for i in range(len(tableros)): 
    #     cuerpo = {'tabla': tableros[i]}
    #     cuerpo['colisiones'] = colisiones(tableros[i], cantidad)
    #     tableros[i] = cuerpo
    # mejores = list(filter(lambda x: x['colisiones'] == 0, tableros))
    pprint(tableros)
    return tableros