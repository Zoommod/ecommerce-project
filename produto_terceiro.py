from cor import CorTexto
from produto import Produto


class ProdutoTerceiro(Produto):
    def __init__(self, nome, codigo, descricao, valor, vendedor):
        super().__init__(nome, codigo, descricao, valor)
        self.__vendedor = vendedor

    def get_vendedor(self):
        return self.__vendedor

    def mostrar_produtos(self):
        super().mostrar_produtos()
        print(f"{CorTexto.CIANO}Vendedor: {CorTexto.BRANCO}{self.get_vendedor()}\n")
        print(f"{CorTexto.AZUL}=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*" * 2)


produto6 = ProdutoTerceiro('Apple Iphone 13', '0006',
                           'O iPhone 13 é um smartphone da Apple lançado em 2021. Ele oferece um design elegante e compacto, com tela OLED brilhante e cores vibrantes. Equipado com o poderoso chip A15 Bionic, o iPhone 13 oferece desempenho excepcional, juntamente com recursos de câmera aprimorados, incluindo modo noturno, Deep Fusion e estabilização de imagem.',
                           3999, 'Vendedor Externo')

produto7 = ProdutoTerceiro('Fire TV Stick 4K', '0007',
                           'O Fire TV Stick 4K é um dispositivo de streaming fabricado pela Amazon. Ele se conecta à sua televisão através da porta HDMI e permite que você transforme sua TV em uma Smart TV, oferecendo acesso a uma ampla variedade de aplicativos de streaming, como Netflix, Amazon Prime Video, Disney+, Hulu e muito mais.',
                           404, 'Vendedor Externo')
