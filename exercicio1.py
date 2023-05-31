def numeros_pares(n):
    numeros_pares = 0
    for number in range(1, n + 1):
        if number % 2 == 0:
            numeros_pares += 1
    return numeros_pares


print(numeros_pares(10))
