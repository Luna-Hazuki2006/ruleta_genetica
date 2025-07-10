import random
from pprint import pprint
tablero = []

def colisiones(lista : list[list[int]]): 
    colisiones = []
    for unico in lista: 
        veces = 0
        for i, cada in enumerate(unico): 
            sumas = cada + 1
            restas = cada - 1
            for j in range(i + 1, len(unico)): 
                if sumas == unico[j] or restas == unico[j]: veces += 2
                sumas += 1
                restas -= 1
        colisiones.append(veces)
    return colisiones

def coronar(cantidad : int = 4): 
    tablero = []
    if cantidad < 4: 
        print('Debe haber al menos 4 reinas')
        return tablero
    pedazos = []
    for _ in range(6): 
        olvidado = list(range(cantidad))
        random.shuffle(olvidado)
        pedazos.append(olvidado)
    cuerpo = {'vector': pedazos}
    cuerpo['fitness'] = colisiones(pedazos)
    cuerpo['∑fitness'] = sum(cuerpo['fitness'])
    cuerpo['probabilidades'] = [esto / cuerpo['∑fitness'] for esto in cuerpo['fitness']]
    cuerpo['probabilidadesAcumuladas'] = [sum(cuerpo['probabilidades'][: i + 1]) for i, _ in enumerate(cuerpo['probabilidades'])]
    tablero.append(cuerpo)
    pprint(cuerpo)
    return tablero