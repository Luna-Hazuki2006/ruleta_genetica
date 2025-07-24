import os
import base64
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx

def grafoicar(nodos : list[str], aristas : list[list[int]], titulo : str):
    valorado = []
    for i, nodo in enumerate(nodos):
        for j, peso in enumerate(aristas[i]):
            if peso != 0:
                valorado.append((nodo, nodos[j], peso)) 
    matplotlib.use('AGG')
    G = nx.Graph()
    # G.add_weighted_edges_from(valorado)
    # G.edges(data=True)
    # fig, ax = plt.subplots(figsize=(1,1))
    for esto in nodos: G.add_node(esto)
    for cada in valorado: G.add_edge(cada[0], cada[1], weight=cada[2])
    elarge = [(u, v) for (u, v, d) in G.edges(data=True)]
    pos = nx.spring_layout(G)
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    # nx.draw(G, with_labels=True, ax=ax)
    # nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    )
    # fig, ax = plt.subplots(figsize=(7,5))
    plt.title(titulo)
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(titulo)
    plt.close()
    legible = ''
    with open(f'{titulo}.png', 'rb') as imagen: 
        pedazos = base64.b64encode(imagen.read())
        legible = pedazos.decode()
    os.remove(f'{titulo}.png')
    legible = 'data:image/png;base64,' + legible
    return {'grafo': legible}