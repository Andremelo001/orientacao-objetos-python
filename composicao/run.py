# Composição: o objeto todo é criado por objetos parte, caso os objetos partes sejam excuidos o todo também será
class Repository:
    def __init__(self):
        self.__insert = Insert() #composição
        self.__select = Select()
    
    def select_by_id(self) -> any:
        self.__insert.insert_value()
        self.__select.by_id()

class Insert:
    def insert_value(self) -> None:
        print("Inserindo o valor no banco")

class Select:
    def by_id(self) -> any:
        print("Buscando id no banco")

repo = Repository()

repo.select_by_id()