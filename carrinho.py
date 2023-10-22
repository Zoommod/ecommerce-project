class Carrinho:

    def __init__(self):
        self.lista_produtos = []
        self.total = 0

    def adicionar_produto(self, produto):
        self.lista_produtos.append(produto)
        self.total += produto.get_valor()
        print(f"\n'{produto.get_nome()}' adicionado ao carrinho.")

    def mostrar_carrinho(self):
        print("CARRINHO DE COMPRAS:\n")
        for produto in self.lista_produtos:
            print(f"Nome: {produto.get_nome()}")
            print(f"Valor: R${produto.get_valor()}\n")
        print(f"Total: R${self.total:.2f}\n")
