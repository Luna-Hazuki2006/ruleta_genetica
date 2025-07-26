import os
import base64
import random
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
from pprint import pprint
import secrets
import time

def obtencion(maximo : float, inicial : list[tuple[str, str]], caminos : list[tuple[str, str, float]]): 
    nuevo = []
    anterior = False
    posterior = False
    alfa = 0
    omega = 0
    cuenta = 0
    while cuenta < maximo and (anterior == False or posterior == False):
        cuenta += 1 
        inicio_trozo = secrets.choice(inicial[1:-3]) if len(inicial) > 4 else secrets.choice(inicial[1:-2])
        alfa = inicial.index(inicio_trozo)
        final_trozo = secrets.choice(inicial[alfa + 1:-2]) if len(inicial) > 4 else secrets.choice(inicial[alfa + 1:-1])
        omega = inicial.index(final_trozo)
        trozo = inicial[alfa:omega + 1]
        trozo = [este[::-1] for este in trozo][::-1]
        nuevo = inicial.copy()
        nuevo[alfa:omega + 1] = trozo
        anterior = obtener_correcto(caminos, nuevo[alfa][0], nuevo[alfa - 1][0])
        posterior = obtener_correcto(caminos, nuevo[omega + 1][1], nuevo[omega][1])
    pprint('resultado')
    pprint(anterior)
    pprint(posterior)
    quitados = []
    agregados = []
    quitados.append(nuevo[alfa - 1])
    nuevo[alfa - 1] = (nuevo[alfa - 1][0], nuevo[alfa][0])
    agregados.append(nuevo[alfa - 1])
    quitados.append(nuevo[omega + 1])
    nuevo[omega + 1] = (nuevo[omega][1], nuevo[omega + 1][1])
    agregados.append(nuevo[omega + 1])
    return anterior, posterior, nuevo, quitados, agregados

def reversar(caminos : list[tuple[str, str, float]], trozo : list[tuple[str, str]]): 
    return [obtener_correcto(caminos, esto) for esto in trozo]

def contar_final(caminos : list[tuple[str, str, float]], trozo : list[tuple[str, str]]): 
    return sum(obtener_correcto(caminos, esto[0], esto[1])[2] for esto in trozo)

def obtener_correcto(caminos : list[tuple[str, str, float]], inicio : str, final : str): 
    real = list(filter(lambda x: inicio in x[:-1] and final in x[:-1], caminos))
    if real == []: return False
    return real[0]

def buscar(caminos : list[tuple[str, str, float]], nodos : list[str]):
    prueba = caminos.copy()
    contados = []
    encontrados = [] 
    inicio = random.choice(caminos)
    prueba.remove(inicio)
    encontrados.append(inicio[:-1])
    contados.append(inicio[0])
    contados.append(inicio[1])
    while len(encontrados) < len(nodos):
        entorno = []
        if len(encontrados) == len(nodos) - 1: 
            entorno = list(filter(lambda x: encontrados[-1][-1] in [x[0], x[1]] 
                                  and encontrados[0][0] in [x[0], x[1]], prueba))
        else: entorno = list(filter(lambda x: encontrados[-1][-1] in [x[0], x[1]] and
                                    x[0] not in contados[:-1] and 
                                    x[1] not in contados[:-1], prueba))
        if entorno == []: return False
        siguiente = entorno[0]
        prueba.remove(siguiente)
        partes = siguiente[:-1]
        if partes[0] != encontrados[-1][-1]: partes = partes[::-1]
        encontrados.append(partes)
        contados.append(partes[-1])
    return encontrados

def obtener_caminos(nodos: list[str], aristas: list[list[int]]): 
    valores = []
    for i, uno in enumerate(nodos[:-1]):
        for este in nodos[i + 1:]: 
            x = nodos.index(uno)
            y = nodos.index(este)
            if aristas[x][y] != 0: valores.append((uno, este, aristas[x][y]))
    return valores

def grafoicar(nodos : list[str], aristas : list[list[int]], titulo : str, 
              optima : list[tuple[str, str, float]] = [], peso : float = 0):
    valorado = obtener_caminos(nodos, aristas)
    matplotlib.use('AGG')
    G = nx.Graph()
    # G.add_weighted_edges_from(valorado)
    # G.edges(data=True)
    # fig, ax = plt.subplots(figsize=(1,1))
    for esto in nodos: G.add_node(esto)
    for cada in valorado: G.add_edge(cada[0], cada[1], weight=cada[2])
    pos = nx.spring_layout(G)
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)
    if optima == []: 
        normales = [(u, v) for (u, v, d) in G.edges(data=True)]
        # edges
        nx.draw_networkx_edges(G, pos, edgelist=normales, width=6)
    else: 
        pprint(optima[0])
        normales = [(u, v) for (u, v, d) in G.edges(data=True) if (u, v) not in optima[0]['trozo'] and (v, u) not in optima[0]['trozo']]
        # edges
        nx.draw_networkx_edges(G, pos, edgelist=normales, width=6)
        nx.draw_networkx_edges(
            G, pos, edgelist=optima[0]['trozo'], width=6, alpha=0.5, edge_color="b", style="dashed"
        )
    # node labels
    # nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    # # edge weight labels
    # edge_labels = nx.get_edge_attributes(G, "weight")
    # nx.draw_networkx_edge_labels(G, pos, edge_labels)
    # # nx.draw(G, with_labels=True, ax=ax)
    # # nx.draw_networkx_labels(G, pos)
    # nx.draw_networkx_edge_labels(
    #     G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    # )
    # node labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    # fig, ax = plt.subplots(figsize=(7,5))
    real = f'{titulo}_{time.time_ns()}'
    plt.title(titulo)
    if optima == []: plt.title(titulo)
    else: plt.title(f'{titulo}: peso = {peso}')
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(real)
    plt.close()
    legible = ''
    with open(f'{real}.png', 'rb') as imagen: 
        pedazos = base64.b64encode(imagen.read())
        legible = pedazos.decode()
    os.remove(f'{real}.png')
    legible = 'data:image/png;base64,' + legible
    return {'grafo': legible}