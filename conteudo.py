# import sys

# numero = input("Digite um número: ")

# print(numero)

# if __name__ == "__main__":
#     for argument in sys.argv:
#         print("Received -> ", argument)

# err = "Arquivo não encontrado"
# print(f"Erro aconteceu: {err}", file=sys.stderr)

# nome = input("Digite seu nome: ")

# for letra in nome:
#     print(letra)

valores = input("Digite numeros naturais separados por um espaço: ")

valores_em_lista = valores.split(" ")

soma_total = 0
for numero in valores_em_lista:
    if numero.isdigit():
        soma_total += int(numero)
    else:
        print(f"Erro ao somar valores, {numero} é um valor inválido")

print(f"A soma dos valores válidos é: {soma_total}")
