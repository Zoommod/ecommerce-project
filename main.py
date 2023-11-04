from produto import produto1, produto2, produto3, produto4, produto5
from produto_terceiro import produto6, produto7
from compra_loja import CompraLoja
from compra import Compra
from cor import CorTexto


lista_codigo_produtos = [produto1.get_codigo(), produto2.get_codigo(), produto3.get_codigo(), produto4.get_codigo(), produto5.get_codigo(), produto6.get_codigo(), produto7.get_codigo()]
carrinho = None

while True:
    print(f"{CorTexto.AZUL}============================")
    print(f"{CorTexto.CIANO}[1] Visualizar Produtos")
    print(f"{CorTexto.CIANO}[2] Adicionar Produto ao Carrinho")
    print(f"{CorTexto.CIANO}[3] Criar Carrinho")
    print(f"{CorTexto.CIANO}[4] Visualizar Carrinho")
    print(f"{CorTexto.CIANO}[5] Retirar Item")
    print(f"{CorTexto.CIANO}[6] Concluir Compra")
    print(f"{CorTexto.CIANO}[0] Sair do Programa")
    print(f"{CorTexto.AZUL}============================")
    opcao = input(str(f"{CorTexto.CIANO}Escolha uma das opções: ")).strip()
    if opcao not in ['0', '1', '2', '3', '4', '5', '6']:
        print(f"\n{CorTexto.VERMELHO}Opção digitada inválida. Tente novamente!")

    if opcao == '1':
        produto1.mostrar_produtos()
        produto2.mostrar_produtos()
        produto3.mostrar_produtos()
        produto4.mostrar_produtos()
        produto5.mostrar_produtos()
        produto6.mostrar_produtos()
        produto7.mostrar_produtos()

    elif opcao == '2':
        codigo_produto = str(input(f"{CorTexto.CIANO}Digite o código do produto a ser adicionado ao carrinho: ")).strip()
        if codigo_produto not in lista_codigo_produtos:
            print(f"\n{CorTexto.VERMELHO}O código digitado não consta em nosso banco de dados. Tente novamente!")

        else:
            if not carrinho:
                tipo_entrega = ''
                while tipo_entrega not in ('1', '2'):
                    if tipo_entrega != '':
                        print(f"{CorTexto.VERMELHO}Opção digitada inválida. Tente novamente!")
                    tipo_entrega = input(f"{CorTexto.CIANO}Digite '1' para entrega em casa ou '2' para retirada na loja: ").strip()
                if tipo_entrega == '1':
                    carrinho = Compra()
                    print(f"\n{CorTexto.VERDE}O carrinho para entrega em casa foi criado com sucesso!")

                elif tipo_entrega == '2':
                    data_retirada = input(f"{CorTexto.CIANO}Digite a data de retirada (dd/mm/aaaa): ")
                    carrinho = CompraLoja(data_retirada)
                    print(f"\n{CorTexto.VERDE}O carrinho para retirada na loja foi criado com sucesso!")

            for produto in [produto1, produto2, produto3, produto4, produto5, produto6, produto7]:
                if produto.get_codigo() == codigo_produto:
                    carrinho.adicionar_produto(produto)

    elif opcao == '3':
        if not carrinho:
            tipo_entrega = ''
            while tipo_entrega not in ('1', '2'):
                if tipo_entrega != '':
                    print(f"{CorTexto.VERMELHO}Opção digitada inválida. Tente novamente!")
                tipo_entrega = input(f"{CorTexto.CIANO}Digite '1' para entrega em casa ou '2' para retirada na loja: ").strip()
            if tipo_entrega == '1':
                carrinho = Compra()
                print(f"\n{CorTexto.VERDE}O carrinho para entrega em casa foi criado com sucesso!")
            elif tipo_entrega == '2':
                data_retirada = input(f"{CorTexto.CIANO}Digite a data de retirada (dd/mm/aaaa): ")
                carrinho = CompraLoja(data_retirada)
                print(f"\n{CorTexto.VERDE}O carrinho para retirada na loja foi criado com sucesso!")
        else:
            print(f"{CorTexto.VERMELHO}O carrinho já foi criado anteriormente!")

    elif opcao == '4':
        if not carrinho:
            print(f"{CorTexto.VERMELHO}O carrinho ainda não foi criado!")
        else:
            carrinho.mostrar_carrinho()

    elif opcao == '5':
        if not carrinho:
            print(f"{CorTexto.VERMELHO}Carrinho ainda não foi criado!")
        else:
            codigo_produto = str(input(f"{CorTexto.CIANO}Digite o código do produto a ser removido do carrinho: ")).strip()
            if codigo_produto not in lista_codigo_produtos:
                print(f"\n{CorTexto.VERMELHO}O código digitado não é de um produto existente. Tente novamente!")
            else:
                for produto in [produto1, produto2, produto3, produto4, produto5, produto5, produto6, produto7]:
                    if produto.get_codigo() == codigo_produto:
                        carrinho.retirar_item(produto)

    elif opcao == '6':
        if not carrinho:
            print(f"\n{CorTexto.VERMELHO}O carrinho ainda não foi criado!")
        else:
            carrinho.concluir_compra()
            carrinho = None

    elif opcao == '0':
        exit()
