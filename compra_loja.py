from carrinho import Carrinho
from cor import CorTexto


class CompraLoja(Carrinho):
    def __init__(self, data_retirada):
        super().__init__()
        self.__data_retirada = data_retirada

    def get_data_retirada(self):
        return self.__data_retirada

    def calcular_total(self):
        return self.total * 0.9

    def mostrar_carrinho(self):
        super().mostrar_carrinho()
        print(f"{CorTexto.CIANO}Data de Retirada: {CorTexto.BRANCO}{self.get_data_retirada()}\n")
        print(f"{CorTexto.CIANO}Total com desconto: {CorTexto.BRANCO}R${self.calcular_total():.2f}\n")

    def concluir_compra(self):
        super().concluir_compra()
        print(f"{CorTexto.CIANO}Total com desconto: {CorTexto.BRANCO}R${self.calcular_total():.2f}\n")
        print(f"{CorTexto.VERDE}Seu pedido estará disponível para retirada na data: {self.get_data_retirada()}")
        print(f"\n{CorTexto.VERDE}COMPRA CONCLUIDA COM SUCESSO!")

