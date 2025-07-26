from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib
import base64
import os
import time

def ver_multiples(menor, mayor, menor_indice, mayor_indice, indices, valores): 
    matplotlib.use('AGG') # Ejemplo de uso
    plt.plot(indices, valores, label='f(x): x^4 - 4x^3 + 4x', color='mediumslateblue')
    plt.scatter(menor_indice, menor, color='green', label='mínimo', zorder=5)
    plt.scatter(mayor_indice, mayor, color='red', label='máximo', zorder=5)

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
    return {'grafo': legible, 'realidad': 'La imagen del rango'}

def obtener(inicio : float, final : float, iteraciones : int, inicial : float, 
            desplazamiento : float, movimientos : int): 
    salto = (final - inicio) / iteraciones
    if inicial > final: return {'grafo': '', 'realidad': 'El punto inicial no puede ser mayor que el final del rangos'}
    resultados = []
    indices = []
    suma = inicio
    for _ in range(iteraciones + 1): 
        indices.append(suma)
        resultados.append(((suma ** 4) - (4 * (suma ** 3)) + (7 * suma)))
        suma += salto
    pasitos = 0
    for i, dado in enumerate(indices): 
        pasitos = i
        if dado <= inicial: break
    
    segmentos = []
    segmentos_datos = []
    pieza = inicial
    trozo = []
    trozo_datos = []
    pprint(inicial)
    pprint(pasitos)
    try: 
        for _ in range(movimientos):
            # trozo = [indices[pasitos]] 
            # trozo_datos = [resultados[pasitos]]
            trozo = []
            trozo_datos = []
            paro = pieza + desplazamiento
            pprint('NOLOSEEEEEEE')
            pprint(pieza)
            pprint(paro)
            # while trozo[-1] < paro: 
            for e, cada in enumerate(indices): 
                if cada >= pieza and cada <= paro:
                    pasitos += 1
                    trozo.append(indices[e])
                    trozo_datos.append(resultados[e])
            segmentos.append(trozo)
            segmentos_datos.append(trozo_datos)
            pieza = paro
    except: 
        # pprint(segmentos)
        segmentos.append(trozo)
        segmentos_datos.append(trozo_datos)
    # pprint(pieza)
    # pprint(segmentos)

    mayores_internos = []
    menores_internos = []
    for esto in segmentos_datos: 
        mayores_internos.append((max(esto), indices[resultados.index(max(esto))]))
        menores_internos.append((min(esto), indices[resultados.index(min(esto))]))

    pprint(mayores_internos)
    pprint(menores_internos)
    
    # pprint(indices)
    # pprint(resultados)
    menor = min(resultados)
    mayor = max(resultados)
    return [menor, 
            indices[resultados.index(menor)], 
            mayor, indices[resultados.index(mayor)], 
            indices, 
            resultados, 
            segmentos, 
            segmentos_datos, 
            mayores_internos, 
            menores_internos]

def mostrar_busqueda(inicio : int, final : int, veces : int, inicial : float, 
            desplazamiento : float, movimientos : int): 
    matplotlib.use('AGG')
    resultado = obtener(inicio, final, veces, inicial, desplazamiento, movimientos)  # Ejemplo de uso
    lista_graficos = []
    lista_graficos.append(ver_multiples(resultado[0], resultado[2], resultado[1], resultado[3], resultado[4], resultado[5]))
    for mayores, menores in zip(resultado[8], resultado[9]): 
        lista_graficos.append(ver_multiples(menores[0], mayores[0], menores[1], mayores[1], resultado[4], resultado[5]))
    return lista_graficos