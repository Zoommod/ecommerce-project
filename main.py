from produto import Produto, produto1, produto2, produto3, produto4, produto5
from carrinho import Carrinho
from compra import Compra
from cor import CorTexto


lista_codigo_produtos = [produto1.get_codigo(), produto2.get_codigo(), produto3.get_codigo(), produto4.get_codigo(), produto5.get_codigo()]
carrinho = None
while True:
    print(f"{CorTexto.AZUL}============================")
    print(f"{CorTexto.CIANO}[1] Visualizar Produtos")
    print(f"{CorTexto.CIANO}[2] Adicionar Produto")
    print(f"{CorTexto.CIANO}[3] Criar Carrinho")
    print(f"{CorTexto.CIANO}[4] Visualizar Carrinho")
    print(f"{CorTexto.CIANO}[5] Retirar Item")
    print(f"{CorTexto.CIANO}[6] Concluir Compra")
    print(f"{CorTexto.AZUL}============================")
    opcao = input(str(f"{CorTexto.CIANO}Escolha uma das opções: "))
    if opcao not in ['1', '2', '3', '4', '5', '6']:
        print(f"\n{CorTexto.VERMELHO}Opção digitada inválida. Tente novamente!")

    if opcao == '1':
        produto1.mostrar_produtos()
        produto2.mostrar_produtos()
        produto3.mostrar_produtos()
        produto4.mostrar_produtos()
        produto5.mostrar_produtos()

    elif opcao == '2':
        if not carrinho:
            carrinho = Carrinho()
            print(f"\n{CorTexto.VERDE}O carrinho foi criado automaticamente!")
        codigo_produto = str(input(f"{CorTexto.CIANO}Digite o código do produto a ser adicionado ao carrinho: "))
        if codigo_produto not in lista_codigo_produtos:
            print(f"\n{CorTexto.VERMELHO}O código digitado não consta em nosso banco de dados. Tente novamente!")
        for produto in [produto1, produto2, produto3, produto4, produto5]:
            if produto.get_codigo() == codigo_produto:
                carrinho.adicionar_produto(produto)

    elif opcao == '3':
        if not carrinho:
            carrinho = Carrinho()
            print(f"\n{CorTexto.VERDE}O carrinho foi criado com sucesso!")
        else:
            print(f"{CorTexto.VERMELHO}O carrinho já foi criado anteriormente!")

    elif opcao == '4':
        if not carrinho:
            print(f"{CorTexto.VERMELHO}Carrinho ainda não foi criado!")
        else:
            carrinho.mostrar_carrinho()

    elif opcao == '5':
        if not carrinho:
            print(f"{CorTexto.VERMELHO}Carrinho ainda não foi criado!")
        else:
            codigo_produto = str(input(f"{CorTexto.CIANO}Digite o código do produto a ser removido do carrinho: "))
            if codigo_produto not in lista_codigo_produtos:
                print(f"\n{CorTexto.VERMELHO}O código digitado não é de um produto existente. Tente novamente!")
            else:
                for produto in [produto1, produto2, produto3, produto4, produto5]:
                    if produto.get_codigo() == codigo_produto:
                        carrinho.retirar_item(produto)

    elif opcao == '6':
        compra = Compra()
        compra.cupom_fiscal(carrinho)