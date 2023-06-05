class TV:
    def __init__(self, tamanho):
        self.__canal = 1
        self.__volume = 50
        self.__tamanho = tamanho
        self.__ligada = False

    def aumentar_volume(self):
        if self.__ligada:
            if self.__volume < 100:
                self.__volume += 1
        else:
            print("A TV está desligada")

    def diminuir_volume(self):
        if self.__ligada:
            if self.__volume > 0:
                self.__volume -= 1
        else:
            print("A TV está desligada")

    def modificar_canal(self, canal):
        if self.__ligada:
            if 1 <= canal <= 100:
                self.__canal = canal
            else:
                raise ValueError("Canal inválido")
        else:
            print("A TV está desligada")

    def ligar_desligar(self):
        self.__ligada = not self.__ligada
