from produto import Produto
from carrinho import Carrinho

produto1 = Produto('Smartphone Galaxy S23 Ultra', '0001',
                   'O Samsung Galaxy S23 Ultra é um smartphone de ponta lançado pela Samsung, oferecendo uma variedade de recursos de alta qualidade. Ele apresenta um design elegante e uma tela AMOLED de alta resolução com taxa \nde atualização aprimorada para uma experiência visual excepcional.',
                   3149)
produto2 = Produto('Monitor Samsung Odyssey Ark', '0002',
                   'O Monitor Samsung Odyssey Ark é uma tela de jogos de alto desempenho projetada especificamente para gamers. Ele oferece uma experiência de jogo imersiva com uma tela curva que envolve o campo de visão do\njogador, proporcionando uma sensação de maior profundidade e envolvimento',
                   3149)
produto3 = Produto('Placa de Vídeo RTX 3060 TI Ventus', '0003',
                   'A GeForce RTX 3060 Ti permite que você jogue os jogos mais recentes usando o poder do Ampere — a arquitetura RTX de segunda geração da NVIDIA. Obtenha desempenho incrível com Ray Tracing Cores e Tensor Cores\naprimorados, novos multiprocessadores de streaming e memória G6X de alta velocidade.',
                   2199)
produto4 = Produto('SSD 1 TB Kingston NV2, M.2 2280 PCIe', '0004',
                   'O NV2 PCIe 4.0 NVMe SSD da Kingston é uma solução substancial de armazenamento de última geração alimentada por um controlador Gen 4x4 NVMe. O NV2 oferece velocidades de leitura/gravação de até 3.500/2.100 MB/s\ncom menores requisitos de energia e menor aquecimento para ajudar a otimizar o desempenho do seu sistema e agregar valor sem sacrifícios.',
                   294)
produto5 = Produto('Processador AMD Ryzen 7 5700X', '0005',
                   'De maneira impressionante, os ganhos de desempenho da arquitetura “Zen 3” podem ser fornecidos sem aumento no consumo de energia ou TDP. A combinação de uma arquitetura de última geração com o processo de 7 nm\nlíder do setor dá ao AMD Ryzen série 5000 uma melhoria de + 24% de geração em eficiência energética e uma impressionante vantagem de 2,8X sobre as arquiteturas concorrentes.',
                   1248)

lista_codigo_produtos = [produto1.codigo, produto2.codigo, produto3.codigo, produto4.codigo, produto5.codigo]
carrinho = None
while True:
    print("============================")
    print("[1] Visualizar Produtos")
    print("[2] Adicionar Produto")
    print("[3] Criar Carrinho")
    print("[4] Visualizar Carrinho")
    print("[5] Retirar Item")
    print("[6] Concluir Compra")
    print("============================")
    opcao = input(str("Escolha uma das opções: "))
    if opcao not in ['1', '2', '3', '4', '5', '6']:
        print("Opção digitada inválida. Tente novamente!")
    if opcao == '1':
        produto1.mostrar_produtos()
        produto2.mostrar_produtos()
        produto3.mostrar_produtos()
        produto4.mostrar_produtos()
        produto5.mostrar_produtos()
    elif opcao == '2':
        if not carrinho:
            carrinho = Carrinho()
            print("O carrinho foi criado automaticamente!")
        codigo_produto = str(input("Digite o código do produto a ser adicionado ao carrinho: "))
        if codigo_produto not in lista_codigo_produtos:
            print("\nO código digitado não consta em nosso banco de dados. Tente novamente!")
        for produto in [produto1, produto2, produto3, produto4, produto5]:
            if produto.codigo == codigo_produto:
                carrinho.adicionar_produto(produto)
    elif opcao == '3':
        if not carrinho:
            carrinho = Carrinho()
        else:
            print("O carrinho já foi criado anteriormente!")
    elif opcao == '4':
        carrinho.mostrar_carrinho()
