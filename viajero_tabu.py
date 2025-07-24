from graficar import grafoicar

def tabues(nodos: list[str], aristas: list[list[int]], titulo: str):
    """
    Función para graficar un grafo utilizando la función grafoicar.
    
    :param nodos: Lista de nodos del grafo.
    :param aristas: Lista de listas que representan las aristas y sus pesos.
    :param titulo: Título para el gráfico.
    :return: Diccionario con la imagen del grafo en formato base64.
    """
    return grafoicar(nodos, aristas, titulo)