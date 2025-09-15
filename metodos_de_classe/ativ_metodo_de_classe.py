class Loja:

    taxa = 100.0

    def __init__(self, valor_produto: float):
        self.valor_produto = valor_produto
    
    def consultar_valor_produto(self):
        valor_produto = self.valor_produto * self.taxa

        print(f"valor do produto {valor_produto}")

    @classmethod
    def editar_taxa_produto(cls, valor: float):
        cls.taxa = valor

loja = Loja(10)
loja_praia = Loja(100)

loja.consultar_valor_produto()

loja_praia.consultar_valor_produto()

loja.editar_taxa_produto(10)

loja.consultar_valor_produto()

loja_praia.consultar_valor_produto()