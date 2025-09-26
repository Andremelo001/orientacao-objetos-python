from abc import ABC, abstractmethod

# Interface: 
class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self) -> None: pass

    @abstractmethod
    def ir_para_casa(self) -> None: pass

    @abstractmethod
    def consultar_beneficios(self) -> None: pass

class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print("O Professor está trabalhando")

    def ir_para_casa(self) -> None:
        print("O Professor está indo para casa")
    
    def consultar_beneficios(self) -> None:
        print("Consultando beneficios da CLT")
    
class ProfessorSubstituto(Trabalhador):
    def trabalhar(self) -> None:
        print("O Professor Substituto está trabalhando")

    def ir_para_casa(self) -> None:
        print("O Professor Substituto está indo para casa")