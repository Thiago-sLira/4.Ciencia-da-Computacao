import random
from collections import Counter

# random_list = random.sample(range(0, 100000), 1000)

# random_list = random.sample(range(0, 100000), random.randint(5, 50))

lista_de_numeros = []

for x in range(10000):
    lista_de_numeros.append(random.randint(0, 1000))

# print(lista_de_numeros)

counter = Counter(lista_de_numeros)

# print(counter[0])

mais_comuns = counter.most_common()

# print(mais_comuns)

elemento_mais_comum, numero_de_vezes = mais_comuns[0]

# print(elemento_mais_comum, numero_de_vezes)

thiago = "pessoa estudante de python"

vogais = "aeiou"

dicas_pythonicas_sao_legais = True


if dicas_pythonicas_sao_legais:
    print("Dicas pythonicas são legais")
else:
    print("Dicas pythonicas não são legais")

nomes_1 = ["Thiago", "João", "Maria"]
nomes_2 = ["Pedro", "José", "Ana", ""]
numeros_1 = [1, 2, 3, 4, 5]
numeros_2 = [6, 7, 8, 9, 10]

ratings = [6, 8, 5, 9, 10]
new_ratings = []

for rating in ratings:
    new_ratings.append(rating * 10)

multiplo_de_tres = [
    new_ratings for new_ratings in new_ratings if new_ratings % 3 == 0]

# print(multiplo_de_tres)

# def imc(peso, altura):
#     return peso / altura ** 2
# (imc(87, 1.92))
