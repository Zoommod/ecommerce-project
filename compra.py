from carrinho import Carrinho


class Compra(Carrinho):
    def __init__(self):
        super().__init__()

    def concluir_compra(self):
        if not self.lista_produtos:
            print("\nO carrinho está vazio. Adicione produtos antes de concluir a compra.")
            return

        print("\nCupom Fiscal:\n")
        for produto in self.lista_produtos:
            print(f"Nome: {produto.get_nome()}, Valor: R${produto.get_valor()}")
        print(f"Total: R${self.total:.2f}")
        print("Compra concluída com sucesso!")
