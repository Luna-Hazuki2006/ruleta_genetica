from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib
import base64
import os
import time

def obtener(inicio : float, final : float, iteraciones : int): 
    salto = (final - inicio) / iteraciones
    resultados = []
    indices = []
    suma = inicio
    for _ in range(iteraciones + 1): 
        indices.append(suma)
        resultados.append(((suma ** 4) - (4 * (suma ** 3)) + (7 * suma)))
        suma += salto
    pprint(indices)
    pprint(resultados)
    menor = min(resultados)
    mayor = max(resultados)
    return [menor, indices[resultados.index(menor)], mayor, indices[resultados.index(mayor)], indices, resultados]

def mostrar_busqueda(inicio : int, final : int, veces : int): 
    matplotlib.use('AGG')
    resultado = obtener(inicio, final, veces)  # Ejemplo de uso
    indices = resultado[4]
    valores = resultado[5]
    plt.plot(indices, valores, label='f(x): x^4 - 4x^3 + 4x', color='mediumslateblue')
    plt.scatter(resultado[1], resultado[0], color='green', label='mínimo', zorder=5)
    plt.scatter(resultado[3], resultado[2], color='red', label='máximo', zorder=5)

    plt.title('Visualización del método de búsqueda local')
    plt.xlabel('rangos')
    plt.ylabel('Resultados')
    plt.grid(True)
    plt.legend()
    titulo = f'busqueda_local_{time.time_ns()}'
    plt.savefig(titulo)
    plt.close()
    legible = ''
    with open(f'{titulo}.png', 'rb') as imagen: 
        pedazos = base64.b64encode(imagen.read())
        legible = pedazos.decode()
    os.remove(f'{titulo}.png')
    legible = 'data:image/png;base64,' + legible
    return {'grafo': legible}