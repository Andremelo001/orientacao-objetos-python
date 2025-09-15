# Classe = aglomerado de atributos(caracteristicas) e métodos(ações) de um contexto específico
class MinhaClasse:
    # Método construtor
    # utilzado para construir os atributos da classe a partir dele
    # roda no momento que a classe é instanciada
    def __init__(self, info: str):
        self.atributo1 = "atributo1"
        self.atributo2 = 10
        self.new_atributo = info

    # Métodos = funções em python
    # self = usado para dizer que o método pertence aquela classe 
    def metodo_1(self):
        print("minha ação")
        print(self.atributo1)

    def metodo_2(self, elem: int):
        print(self.atributo2 + elem)

    def metodo_3(self):
        self.metodo_1()

#objeto        #classe -> a partir de uma classe instanciamos um objeto
minha_classe = MinhaClasse("test de new atributo")

minha_classe.metodo_1()

minha_classe.metodo_2(10)

minha_classe.metodo_3()