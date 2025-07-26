import random
import secrets

matriz_total = []

def binarear(lista : list, i : int):
    dato = lista[i]
    # pprint(dato)
    binario = list(f'{dato:b}')
    # pprint(binario)
    lugar = random.randrange(0, len(binario))
    binario[lugar] = '0' if binario[lugar] == '1' else '1'
    binario = ''.join(binario)
    # pprint(binario)
    final = int(binario, 2)
    # pprint(final)
    return final

def bicombinado(lista : list, a : int, b : int): 
    primero = list(f'{lista[a]:b}')
    segundo = list(f'{lista[b]:b}')
    if len(primero) > len(segundo): 
        mayor = len(primero) - len(segundo)
        segundo = list('0' * mayor) + segundo
    elif len(primero) < len(segundo): 
        mayor = len(segundo) - len(primero)
        primero = list('0' * mayor) + primero
    lugar = random.randrange(1, len(primero) + 1)
    supa = primero[:lugar]
    suba = primero[lugar:]
    supb = segundo[:lugar]
    subb = segundo[lugar:]
    penultimo = supa + subb
    ultimo = supb + suba
    penultimo = ''.join(penultimo)
    ultimo = ''.join(ultimo)
    penultimo = int(penultimo, 2)
    ultimo = int(ultimo, 2)
    return penultimo, ultimo
    # alfa = random.randrange(1, len(primero) - 1)
    # omega = random.randrange(1, len(segundo) - 1)
    # supa = primero[:alfa]
    # suba = primero[alfa:]
    # supb = segundo[:omega]
    # subb = segundo[omega:]
    # penultimo = supa + subb
    # ultimo = supb + suba
    # penultimo = ''.join(penultimo)
    # ultimo = ''.join(ultimo)
    # penultimo = int(penultimo, 2)
    # ultimo = int(ultimo, 2)
    # return penultimo, ultimo

def ruletear(lista): 
    lista['fitness'] = [((x ** 4) - (4 * (x ** 3)) + (7 * x)) + 0.1 for x in lista['vector']]
    lista['∑fitness'] = sum(lista['fitness'])
    lista['probabilidades'] = [esto / lista['∑fitness'] for esto in lista['fitness']]
    lista['probabilidadesAcumuladas'] = [sum(lista['probabilidades'][: i + 1]) for i, _ in enumerate(lista['probabilidades'])]
    return lista

def seleccionar(lista): 
    aleatorio = random.random()
    i = 0
    for i, esto in enumerate(lista): 
        if aleatorio <= esto: break 
    return i

def genetico(inicio : int, final : int, veces : int, generaciones : int): 
    matriz_total = []
    if inicio >= final: 
        print('El valor inicial no puede ser mayor al valor final')
        return matriz_total
    elif veces <= 0: 
        print('Debe haber una cantidad de iteraciones mayor a 0')
        return matriz_total
    elif generaciones <= 0: 
        print('Debe tener mas de una generación')
        return matriz_total
    # matriz_total.append({'vector': [random.randrange(inicio, final) for _ in range(veces)]})
    matriz_total.append({'vector': [secrets.choice(range(inicio, final + 1)) for _ in range(veces)]})
    lista = ruletear(matriz_total[-1])
    matriz_total[-1] = lista
    for _ in range(generaciones): 
        cuerpo = {'vector': []}
        cuerpo['padres'] = []
        # pedazos : dict[str, list] = matriz_total[-1]
        # pprint(pedazos)
        acumulado = []
        vectores = []
        acumulado.extend(matriz_total[-1]['probabilidadesAcumuladas'])
        vectores.extend(matriz_total[-1]['vector'])
        for __ in range(veces): 
            decision = random.random()
            if decision > 0.1:
                a = seleccionar(acumulado)
                b = seleccionar(acumulado)
                while a == b: 
                    a = seleccionar(acumulado)
                    b = seleccionar(acumulado)
                alfa = [vectores[a], vectores[b]]
                primer, segundo = bicombinado(vectores, a, b)
                if len(cuerpo['vector']) == veces: break
                cuerpo['padres'].append(alfa)
                cuerpo['vector'].append(primer)
                if len(cuerpo['vector']) == veces: break
                cuerpo['vector'].append(segundo)
                cuerpo['padres'].append(alfa)
            else: 
                # pprint(pedazos['probabilidadesAcumuladas'])
                i = seleccionar(acumulado)
                dato = binarear(vectores, i)
                if len(cuerpo['vector']) == veces: break
                cuerpo['vector'].append(dato)
                cuerpo['padres'].append([vectores[i]])
                if len(cuerpo['vector']) == veces: break
                # acumulado.pop(i)
                # vectores.pop(i)
                # pedazos['probabilidadesAcumuladas'].pop(i)
                # pedazos['vector'].pop(i)
        # pprint(cuerpo)
        cuerpo = ruletear(cuerpo)
        matriz_total.append(cuerpo)
    # matriz_total[-1]['']
    # pprint(matriz_total)
    return matriz_total