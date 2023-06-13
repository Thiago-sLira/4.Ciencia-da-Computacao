# escrita
with open("arquivo.txt", "w") as file:
    LINES = ["Olá\n", "mundo\n", "belo\n", "do\n", "Python\n"]
    file.writelines(LINES)

# leitura
try:
    with open("arquivo.txt", "r") as file:
        # for line in file:
        print(file.read().splitlines())
except FileNotFoundError:
    print("Arquivo não encontrado")
