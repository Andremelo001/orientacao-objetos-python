# Agregação: uma classe nao depende da outra para existir, elas apenas se relacionam

class Produto:
    def __init__(self, nome: str, valor: int) -> None:
        self.__nome = nome
        self.__valor = valor
    
    def info_produto(self) -> None:
        print(f"Produto: {self.__nome}, Valor: {self.__valor}")

class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []
    
    def adicionar_produtos(self, produto: Produto) -> None:
        self.__produtos.append(produto)
    
    def finalizar_compra(self) -> None:

        print(f"Sua compra foi finalizada com sucesso!")
        for produto in self.__produtos:
            produto.info_produto()

agua = Produto("agua", 2)
maca = Produto("maca", 4)

cc = CarrinhoDeCompras()

cc.adicionar_produtos(agua)
cc.adicionar_produtos(maca)

cc.finalizar_compra()