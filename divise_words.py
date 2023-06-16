text = [
    "Ana",
    "ama",
    "Joao",
    "que",
    "ama",
    "Jose",
    "mais",
    "Jose",
    "nao",
    "ama",
    "Ana",
]


def screening(text):
    words_divised = {}

    for word in text:
        first_char = word[0].lower()
        if first_char not in words_divised:
            words_divised[first_char] = [word]
        else:
            words_divised[first_char].append(word)

    return words_divised
