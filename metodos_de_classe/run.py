class MinhaClasse:

    #atributo de classe
    #valor geral para todos
    estatico = "de"

    def __init__(self, estado) -> True:
        self.__estado = estado
    
    def print_variavel_de_classe(self):
        print(self.estatico)
    
    # Método de classe
    # Altera a classe
    @classmethod
    def alteracao_variavel_de_classe(cls):
        cls.estatico = "demelo"
        # MinhaClasse.estatico = "demelo"

obj = MinhaClasse(True)

obj.alteracao_variavel_de_classe()

print(obj.estatico)

print(MinhaClasse.estatico)