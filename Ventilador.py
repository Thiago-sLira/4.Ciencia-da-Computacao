class Ventilador:
    @property
    def cor(self):
        return self.__cor.upper()

    @cor.setter
    def cor(self, nova_cor):
        if nova_cor.lower() == "turquesa":
            raise ValueError("Não existe liquidificador turquesa")
        self.__cor = nova_cor

    def __init__(self, cor, potencia, tensao, preco):
        self.cor = cor
        self.potencia = potencia
        self.tensao = tensao
        self.preco = preco

    def __str__(self):
        return f"Ventilador {self.cor} de {self.potencia}W"
