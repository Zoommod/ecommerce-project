from cor import CorTexto


class Produto:
    def __init__(self, nome, codigo, descricao, valor):
        self.__nome = nome
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor

    def get_nome(self):
        return self.__nome

    def get_codigo(self):
        return self.__codigo

    def get_descricao(self):
        return self.__descricao

    def get_valor(self):
        return self.__valor

    def mostrar_produtos(self):
        print(f"\n{CorTexto.CIANO}Nome: {CorTexto.BRANCO}{self.get_nome()}")
        print(f"{CorTexto.CIANO}Código: {CorTexto.BRANCO}{self.get_codigo()}")
        print(f"{CorTexto.CIANO}Descrição: {CorTexto.BRANCO}{self.get_descricao()}")
        print(f"{CorTexto.CIANO}Valor: {CorTexto.BRANCO}R${self.get_valor()}\n")
        print(f"{CorTexto.AZUL}=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*" * 2)


produto1 = Produto('Smartphone Galaxy S23 Ultra', '0001',
                   'O Samsung Galaxy S23 Ultra é um smartphone de ponta lançado pela Samsung, oferecendo uma variedade de recursos de alta qualidade. Ele apresenta um design elegante e uma tela AMOLED de alta resolução com taxa \nde atualização aprimorada para uma experiência visual excepcional.',
                   3149)
produto2 = Produto('Monitor Gamer Samsung Odyssey G32A', '0002',
                   'O AMD FreeSync Premium apresenta tecnologia de sincronização adaptável, que reduz o travamento de tela, oscilação e atrasos. Gire, incline e ajuste seu monitor até que todos os inimigos estejam perfeitamente\nvisíveis. Sua tela pode ser movida livremente para que você encontre conforto total no jogo.',
                   1159)
produto3 = Produto('Placa de Vídeo RTX 3060 TI Ventus', '0003',
                   'A GeForce RTX 3060 Ti permite que você jogue os jogos mais recentes usando o poder do Ampere — a arquitetura RTX de segunda geração da NVIDIA. Obtenha desempenho incrível com Ray Tracing Cores e Tensor Cores\naprimorados, novos multiprocessadores de streaming e memória G6X de alta velocidade.',
                   2199)
produto4 = Produto('SSD 1 TB Kingston NV2, M.2 2280 PCIe', '0004',
                   'O NV2 PCIe 4.0 NVMe SSD da Kingston é uma solução substancial de armazenamento de última geração alimentada por um controlador Gen 4x4 NVMe. O NV2 oferece velocidades de leitura/gravação de até 3.500/2.100 MB/s\ncom menores requisitos de energia e menor aquecimento para ajudar a otimizar o desempenho do seu sistema e agregar valor sem sacrifícios.',
                   294)
produto5 = Produto('Processador AMD Ryzen 7 5700X', '0005',
                   'De maneira impressionante, os ganhos de desempenho da arquitetura “Zen 3” podem ser fornecidos sem aumento no consumo de energia ou TDP. A combinação de uma arquitetura de última geração com o processo de 7 nm\nlíder do setor dá ao AMD Ryzen série 5000 uma melhoria de + 24% de geração em eficiência energética e uma impressionante vantagem de 2,8X sobre as arquiteturas concorrentes.',
                   1248)
