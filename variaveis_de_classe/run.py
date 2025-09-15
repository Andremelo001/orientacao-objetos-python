class MinhaClasse:

    #atributo de classe
    #valor geral para todos
    estatico = "de" # de -> dev

    def __init__(self, estado) -> True:
        self.__estado = estado

obj = MinhaClasse(True) # dev -> devPython
obj1 = MinhaClasse(True) # dev

#altera para todos - tando para os objs quanto para a classe
MinhaClasse.estatico = "dev"

#altera apenas para os objetos
obj.estatico = "devPython"

print(obj.estatico)

print(obj1.estatico)

print(MinhaClasse.estatico)