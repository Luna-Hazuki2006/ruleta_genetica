from graficar import grafoicar, obtener_caminos, buscar, contar_final, obtencion
from pprint import pprint
import random
import math
import secrets

# def obtencion(maximo : float, inicial : list[tuple[str, str]], caminos : list[tuple[str, str, float]]): 
#     nuevo = []
#     alfa = False
#     omega = False
#     indice = 0
#     andice = 0
#     cuenta = 0
#     while cuenta < maximo and (alfa == False or omega == False):
#         cuenta += 1 
#         derecha = inicial[1:-3] if len(inicial) > 4 else inicial[1:-2]
#         alfa = random.random()
#         anterior = secrets.choice(derecha)
#         indice = inicial.index(anterior)
#         izquierda = inicial[indice + 1:-2] if len(inicial) > 4 else inicial[indice + 1:-1]
#         posterior = secrets.choice(izquierda)
#         andice = inicial.index(posterior)
#         trozo = inicial[indice:andice + 1]
#         trozo = [este[::-1] for este in trozo][::-1]
#         nuevo = inicial.copy()
#         nuevo[indice:andice + 1] = trozo
#         alfa = obtener_correcto(caminos, nuevo[indice][0], nuevo[indice - 1][0])
#         omega = obtener_correcto(caminos, nuevo[andice + 1][1], nuevo[andice][1])
#     return alfa, omega, nuevo

def recocer(nodos: list[str], aristas: list[list[int]], titulo: str):
    """
    Función para graficar un grafo utilizando la función grafoicar.
    
    :param nodos: Lista de nodos del grafo.
    :param aristas: Lista de listas que representan las aristas y sus pesos.
    :param titulo: Título para el gráfico.
    :return: Diccionario con la imagen del grafo en formato base64.
    """
    rutas = []
    caminos = obtener_caminos(nodos, aristas)
    nodado = len(nodos)
    actual = len(caminos)
    pprint(caminos)
    pprint(actual)
    pprint(nodado)
    inicial = []
    cuerpo = {}
    maximo = (nodado * (nodado - 1)) / 2
    if actual != 0 and actual >= nodado: 
        for _ in range(nodado * 2): 
            inicial = buscar(caminos, nodos)
            if inicial != False: break
        pprint(inicial)
    if inicial != False and inicial != []: 
        peso = contar_final(caminos, inicial)
        temperatura = peso * 0.2
        cuerpo['trozo'] = inicial.copy()
        cuerpo['peso'] = peso
        cuerpo['temperatura'] = temperatura
        rutas.append(cuerpo)
        continuar = True
        veces = 0
        pruebas = 0
        while continuar and pruebas < maximo: 
            pruebas += 1
            cuerpo = {}
            anterior, posterior, nuevo, quitados, agregados = obtencion(maximo, rutas[-1]['trozo'], caminos)
            pprint(anterior)
            pprint(posterior)
            pprint(nuevo)
            if anterior == False or posterior == False: continue
            cuerpo['trozo'] = nuevo.copy()
            cuerpo['peso'] = contar_final(caminos, cuerpo['trozo'])
            cuerpo['temperatura'] = 0.5 * rutas[-1]['temperatura']
            if cuerpo['peso'] < list(sorted(rutas, key=lambda x: x['peso']))[0]['peso']: 
                veces = 0
                rutas.append(cuerpo)
            else: 
                veces += 1
                # temperatura = 0.2 * cuerpo['peso']
                x = (list(sorted(rutas, key=lambda x: x['peso']))[0]['peso'] - cuerpo['peso']) / cuerpo['temperatura']
                exponencial = math.exp(x)
                if random.random() < exponencial: rutas.append(cuerpo)
                if veces >= 5: continuar = False
    pprint(rutas)
    if len(rutas) > 1: 
        ordenadas = sorted(rutas[1:], key=lambda x: x['peso'])
        return grafoicar(nodos, aristas, titulo, ordenadas, ordenadas[0]['peso'])
    return grafoicar(nodos, aristas, titulo)