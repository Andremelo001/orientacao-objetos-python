from abc import ABC, abstractmethod

class InterfaceElemento(ABC):

    @abstractmethod
    def executar(self) -> None: pass