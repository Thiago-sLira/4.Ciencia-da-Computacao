def maior_numero(numero1, numero2):
    if numero1 > numero2:
        return numero1
    else:
        return numero2


lista = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27, 1]
lista_de_nomes = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]


def media_aritmetica():
    soma = 0
    for numero in lista:
        soma += numero
    return soma / len(lista)


def imprime_quadrado(n):
    for i in range(n):
        print("*" * n)


def maior_nome(lista):
    maior_nome = ""
    for nome in lista:
        if len(nome) > len(maior_nome):
            maior_nome = nome
    return maior_nome


def quantidade_de_tinta(metros_quadrados):
    """1 litro para 3 ** 2, 1 lata de 18 litros = 80.00"""
    can_price = 80
    required_liters = metros_quadrados / 3
    required_cans = required_liters // 18
    if required_liters % 18:
        required_cans += 1
    return required_cans, required_cans * can_price


def type_of_triangle(s1, s2, s3):
    is_triangle = (
        s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2
    )
    if not is_triangle:
        return "não é triângulo"
    elif s1 == s2 == s3:
        return "equilátero"
    elif s1 == s2 or s2 == s3 or s1 == s3:
        return "isósceles"
    else:
        return "escaleno"


def menor_elemento(lista):
    return min(lista)


def imprime_triangulo(n):
    lista = range(n)
    for i in lista:
        print("*" * i)


def somatoria(N):
    lista = range(N + 1)
    soma = 0
    for numero in lista:
        soma += numero
    return soma


def valor_combustivel(litros, tipo):
    # tipos = {"G": 2.50, "A": 1.90}
    gasolina_preco = 2.50
    alcool_preco = 1.90
    if tipo == "G":
        if litros <= 20:
            return (0.03 * gasolina_preco) * litros
        else:
            return (0.05 * gasolina_preco) * litros
    else:
        if litros <= 20:
            return (0.04 * alcool_preco) * litros
        else:
            return (0.06 * alcool_preco) * litros


print(somatoria(5))
print({"G": 2.50, "A": 1.90}["G"])
