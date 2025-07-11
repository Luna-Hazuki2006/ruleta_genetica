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

def llenar(cuerpo : dict): 
    cuerpo['colisiones'] = colisiones(cuerpo['vector'])
    total = len(cuerpo['vector'][0])
    real = total * (total - 1)
    cuerpo['fitness'] = [(real - esto) + 0.1 for esto in cuerpo['colisiones']]
    cuerpo['∑fitness'] = sum(cuerpo['fitness'])
    cuerpo['probabilidades'] = [esto / cuerpo['∑fitness'] for esto in cuerpo['fitness']]
    cuerpo['probabilidadesAcumuladas'] = [sum(cuerpo['probabilidades'][: i + 1]) for i, _ in enumerate(cuerpo['probabilidades'])]
    return cuerpo

def seleccionar(lista): 
    aleatorio = random.random()
    i = 0
    for i, esto in enumerate(lista): 
        if aleatorio <= esto: break 
    return i

def mutar(vector : list[int]): 
    a = 0
    b = 0
    while a == b:
        a = random.randrange(0, len(vector))
        b = random.randrange(0, len(vector))
    vector[a], vector[b] = vector[b], vector[a]
    return vector

def cruzar(primero : list[int], segundo : list[int]):
    pass

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
    cuerpo = llenar(cuerpo)
    tablero.append(cuerpo)
    for _ in range(6): 
        cuerpo = {'vector': []}
        acumulado = []
        vectores = []
        acumulado.extend(tablero[-1]['probabilidadesAcumuladas'])
        vectores.extend(tablero[-1]['vector'])
        for __ in range(6): 
            # decision = random.random()
            # if decision > 0.1: 
            #     a = 0
            #     b = 0
            #     while a == b: 
            #         a = seleccionar(acumulado)
            #         b = seleccionar(acumulado)
            #     primer, segundo = cruzar(vectores[a], vectores[b])
            #     if len(cuerpo['vector']) == 6: break
            #     cuerpo['vector'].append(primer)
            #     if len(cuerpo['vector']) == 6: break
            #     cuerpo['vector'].append(segundo)
            # else: 
                i = seleccionar(acumulado)
                dato = mutar(vectores[i])
                if len(cuerpo['vector']) == 6: break
                cuerpo['vector'].append(dato)
                if len(cuerpo['vector']) == 6: break
        cuerpo = llenar(cuerpo)
        tablero.append(cuerpo)
    pprint(cuerpo)
    return tablero