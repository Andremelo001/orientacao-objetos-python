class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None
    
    # Método para "setar" o valor
    def setter(self, valor: int) -> None:
        self.__valor = valor

    # Método para mostrar o valor
    def getter(self) -> int:
        return self.__valor
    
my_class = MinhaClasse()

my_class.setter(10)

valor = my_class.getter()

print(valor)