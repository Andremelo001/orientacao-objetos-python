from abc import ABC, abstractmethod

# Interface: 
class Trabalhador(ABC):

    @abstractmethod
    def trabalhar(self) -> None: pass

    @abstractmethod
    def ir_para_casa(self) -> None: pass

    @abstractmethod
    def horario_de_almoco(self) -> None: pass

class Pessoa(Trabalhador):

    def trabalhar(self) -> None:
        print("O Professor está trabalhando")

    def ir_para_casa(self) -> None:
        print("O Professor está indo para casa")

    def horario_de_almoco(self) -> None:
        print("O Professor está almoçando")


def comunicar_o_trabalhador(trabalhador: Trabalhador):
    trabalhador.trabalhar()
    print("Comunicar o trabalhador")
    trabalhador.horario_de_almoco()
    trabalhador.trabalhar()
    print("Comunicar o trabalhador")
    trabalhador.ir_para_casa()

p1 = Pessoa()

comunicar_o_trabalhador(p1)
