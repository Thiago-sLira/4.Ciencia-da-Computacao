class Estatistca:
    def __init__(self, lista):
        self.__lista = lista

    def media(self):
        return sum(self.__lista) / len(self.__lista)

    def mediana(self):
        if len(self.__lista) % 2 == 0:
            return (
                self.__lista[len(self.__lista) // 2]
                + self.__lista[len(self.__lista) // 2 - 1]
            ) / 2
        else:
            return self.__lista[len(self.__lista) // 2]

    def moda(self):
        return max(set(self.__lista), key=self.__lista.count)
