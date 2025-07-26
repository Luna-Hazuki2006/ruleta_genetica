from graficar import grafoicar, obtener_caminos, buscar, contar_final, obtencion
from pprint import pprint
import random
import secrets

def tabues(nodos: list[str], aristas: list[list[int]], titulo: str):
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
        cuerpo['trozo'] = inicial.copy()
        cuerpo['peso'] = contar_final(caminos, inicial)
        cuerpo['quitados'] = []
        cuerpo['agregados'] = []
        rutas.append(cuerpo)
        for _ in range(int(maximo)): 
            cuerpo = {}
            anterior, posterior, nuevo, quitados, agregados = obtencion(maximo, rutas[-1]['trozo'], caminos)
            pprint(anterior)
            pprint(posterior)
            pprint(nuevo)
            if anterior == False or posterior == False: continue
            cuerpo['trozo'] = nuevo.copy()
            cuerpo['peso'] = contar_final(caminos, nuevo)
            cuerpo['quitados'] = quitados.copy()
            cuerpo['agregados'] = agregados.copy()
            rutas.append(cuerpo)
    # pprint(rutas)
    if len(rutas) > 1: 
        ordenadas = sorted(rutas[1:], key=lambda x: x['peso'])
        return grafoicar(nodos, aristas, titulo, ordenadas, ordenadas[0]['peso'])
    return grafoicar(nodos, aristas, titulo)