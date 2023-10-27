from carrinho import Carrinho
from cor import CorTexto


class Compra(Carrinho):
    def __init__(self):
        super().__init__()

    def concluir_compra(self):
        if not self.lista_produtos:
            print(f"\n{CorTexto.VERMELHO}O carrinho está vazio. Adicione produtos antes de concluir a compra.")
            return

        print("\nCUPOM FISCAL:\n")
        for produto in self.lista_produtos:
            print(f"{CorTexto.CIANO}Nome: {CorTexto.BRANCO}{produto.get_nome()}")
            print(f"{CorTexto.CIANO}Valor: {CorTexto.BRANCO}R${produto.get_valor()}\n")

        print(f"{CorTexto.CIANO}Total: {CorTexto.BRANCO}R${self.total:.2f}\n")
        print(f"\n{CorTexto.VERDE}COMPRA CONCLUIDA COM SUCESSO!")
