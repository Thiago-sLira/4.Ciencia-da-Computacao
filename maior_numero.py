def maior_numero(list):
    numero = 0
    for index in list:
        if index > numero:
            numero = index
    return numero


lista = [1, 2, 3, 4, 5, 6, 50]

print(maior_numero(lista))
