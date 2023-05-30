import random
import json

with open("jogo.json") as file:
    words = json.load(file)["palavras"]

word = (random.choice(words))

scrambled_word = "".join(random.sample(word, len(word)))

tries = 0

win = False

while not win:
    print(f"Qual é essa palavra? ---> {scrambled_word}")
    print(f"Você tem {3 - tries} tentativas!")
    palavraDigitada = input()

    if palavraDigitada == word:
        print(f"Parabens, você acertou a palavra: {palavraDigitada}")
        win = True
        break
    elif palavraDigitada != word and tries < 2:
        print(f"Ops!! {palavraDigitada} não é a palavra certa")
        tries += 1
    else:
        print(f"Tentativas excedidas, a palavra era: {word}")
        break
