def colisiones(lista : list[int] | tuple[int], cantidad : int): 
    veces_uno = 0
    for i, cada in enumerate(lista[:cantidad]): 
        positivo = True
        negativo = True
        sumas = cada + 1
        restas = cada - 1
        for j in range(i + 1, len(lista)): 
            if sumas == lista[j] and positivo: 
                veces_uno += 2
                positivo = False
            if restas == lista[j] and negativo: 
                veces_uno += 2
                negativo = False
            sumas += 1
            restas -= 1
    return veces_uno