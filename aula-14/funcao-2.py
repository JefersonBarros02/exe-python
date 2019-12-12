def pares_intervalo(inicio_intervalo, fim_intervalo):
    lista_numeros = []
    for num in range(inicio_intervalo, fim_intervalo + 1):
        if num % 2 == 0:
            lista_numeros += [num]
    return lista_numeros


print(pares_intervalo(1, 10))
