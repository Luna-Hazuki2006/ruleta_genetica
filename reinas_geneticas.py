import random
from pprint import pprint
from colisiones import colisiones
import math

# def colisiones(lista : list[list[int]]): 
#     encuentros = []
#     for unico in lista: 
#         veces = 0
#         for i, cada in enumerate(unico): 
#             positivo = True
#             negativo = True
#             sumas = cada + 1
#             restas = cada - 1
#             for j in range(i + 1, len(unico)): 
#                 if sumas == unico[j] and positivo: 
#                     veces += 2
#                     positivo = False
#                 if restas == unico[j] and negativo: 
#                     veces += 2
#                     negativo = False
#                 sumas += 1
#                 restas -= 1
#         encuentros.append(veces)
#     return encuentros

def llenar(cuerpo : dict): 
    total = len(cuerpo['vector'][0])
    cuerpo['colisiones'] = []
    for cada in cuerpo['vector']: 
        cuerpo['colisiones'].append(colisiones(cada, total))
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
    penultimo = []
    ultimo = []
    for cada, uno in zip(primero, segundo): 
        if (len(penultimo) != len(primero) and
            cada not in penultimo): 
            penultimo.append(cada)
        if (len(penultimo) != len(primero) and
            uno not in penultimo): 
            penultimo.append(uno)
        if (len(ultimo) != len(segundo) and
            uno not in ultimo): 
            ultimo.append(uno)
        if (len(ultimo) != len(segundo) and
            cada not in ultimo): 
            ultimo.append(cada)
        if len(penultimo) == len(primero) and len(ultimo) == len(segundo): break
    return penultimo, ultimo

def coronar(cantidad : int = 4): 
    generaciones = random.randrange(1000, 3000)
    poblaciones = math.factorial(cantidad)
    tablero = []
    if cantidad < 4: 
        print('Debe haber al menos 4 reinas')
        return tablero
    pedazos = []
    for _ in range(poblaciones): 
        olvidado = list(range(cantidad))
        random.shuffle(olvidado)
        pedazos.append(olvidado)
    unidad = {'vector': pedazos}
    cuerpo_inicial = llenar(unidad)
    tablero.append(cuerpo_inicial)
    for _ in range(generaciones): 
        cuerpo = {'vector': []}
        acumulado = []
        vectores = []
        acumulado.extend(tablero[-1]['probabilidadesAcumuladas'])
        vectores.extend(tablero[-1]['vector'])
        for __ in range(poblaciones): 
            decision = random.random()
            if decision > 0.1: 
                a = 0
                b = 0
                while a == b: 
                    a = seleccionar(acumulado)
                    b = seleccionar(acumulado)
                primer, segundo = cruzar(vectores[a], vectores[b])
                if len(cuerpo['vector']) == poblaciones: break
                cuerpo['vector'].append(primer)
                if len(cuerpo['vector']) == poblaciones: break
                cuerpo['vector'].append(segundo)
            else: 
                i = seleccionar(acumulado)
                dato = mutar(vectores[i])
                if len(cuerpo['vector']) == poblaciones: break
                cuerpo['vector'].append(dato)
                if len(cuerpo['vector']) == poblaciones: break
        cuerpo_final = llenar(cuerpo)
        pprint(cuerpo_final)
        tablero.append(cuerpo_final)
    # pprint(tablero)
    return tablero