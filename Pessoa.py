from Liquidificador import Liquidificador
from Ventilador import Ventilador


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.liquidificador = None
        self.ventilador = None

    def comprar_liquidificador(self, liquidificador):
        if liquidificador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= liquidificador.preco
            self.liquidificador = liquidificador

    def comprar_ventilador(self, ventilador):
        if ventilador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= ventilador.preco
            self.ventilador = ventilador

    def __str__(self):
        return f"""
            {self.nome} - possui {self.saldo_na_conta} reais em sua conta,
            um {self.liquidificador},
            um {self.ventilador}
            """


liquidificador_vermelho = Liquidificador("Rosa", "110", "127", 200)
ventilador_azul = Ventilador("Azul", "110", "127", 200)
pessoa_cozinheira = Pessoa("Jacquin", 1000)
pessoa_cozinheira.comprar_liquidificador(liquidificador_vermelho)
pessoa_cozinheira.comprar_ventilador(ventilador_azul)
print(pessoa_cozinheira)
