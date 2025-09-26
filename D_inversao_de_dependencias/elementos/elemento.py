from elementos.interfaces.elemento_interface import InterfaceElemento

class Elemento(InterfaceElemento):
    def executar(self) -> None:
        print("Estou executando o elemento")
