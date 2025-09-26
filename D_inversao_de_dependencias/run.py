from elementos.interfaces.elemento_interface import InterfaceElemento
from elementos.elemento import Elemento

class Principal():
    def __init__(self, elemento: InterfaceElemento) -> None:
        self.__elem = elemento
    
    def run(self) -> None:
        self.__elem.executar()
        print("Estou executando a classe principal")
    

elem = Elemento()

cl1 = Principal(elem)

cl1.run()