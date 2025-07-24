import math
import random
from colisiones import colisiones

def recocer(cantidad : int = 4): 
    tableros = []
    inicial = list(range(cantidad))
    random.shuffle(inicial)
    choques = colisiones(inicial, cantidad)
    pedazo = {
        'tablero': inicial, 
        'colisiones': choques
    }
    tableros.append(pedazo)
    continuar = True
    veces = 0
    while continuar: 
        primero = random.randrange(0, cantidad)
        segundo = random.randrange(0, cantidad)
        while primero == segundo: 
            primero = random.randrange(0, cantidad)
            segundo = random.randrange(0, cantidad)
        creacion = []
        creacion.extend(tableros[-1]['tablero'])
        creacion[primero], creacion[segundo] = creacion[segundo], creacion[primero]
        choques = colisiones(creacion, cantidad)
        if choques < tableros[-1]['colisiones']: 
            veces = 0
            tableros.append({'tablero': creacion, 'colisiones': choques})
        else: 
            veces += 1
            temperatura = 0.2 * choques
            x = (choques - tableros[-1]['colisiones']) / temperatura
            exponencial = math.exp(x)
            if random.random() < exponencial: tableros.append({'tablero': creacion, 'colisiones': choques})
            if veces >= 5: continuar = False
    tableros.sort(key=lambda x: x['colisiones'])
    return tableros