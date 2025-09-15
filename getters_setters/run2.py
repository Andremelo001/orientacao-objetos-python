class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = 10
    
    # Método para "setar" o valor
    def setter(self, valor: int) -> None:
        self.__valor = valor

    # Método para mostrar o valor
    @property
    def getter(self) -> int:
        return self.__valor
    
my_class = MinhaClasse()

print(my_class.getter)