class Produto:
    def __init__(self, nome, codigo, descricao, valor):
        self.nome = nome
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor

    def mostrar_produtos(self):
        print(f"\nNome: {self.nome}")
        print(f"Código: {self.codigo}")
        print(f"Descrição: {self.descricao}")
        print(f"Valor: {self.valor}\n")
        print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"*2)
