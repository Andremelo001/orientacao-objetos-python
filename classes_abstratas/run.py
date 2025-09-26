# biblioteca de classes abstratas
from abc import ABC, abstractmethod

# classe abstrata: Não possui objetos
# porem pode ser herdada por outras classes
class Pessoa(ABC):
    def correr(self):
        print("A pessoa esta correndo de manha")

    # métodos abstratos
    # classes filhas DEVEM criar esse método
    @abstractmethod
    def trabalhar(self): pass

# erro
# p1 = Pessoa()

class Professor(Pessoa):
    def trabalhar(self):
        print("O professor esta dando aula")

class Cozinheiro(Pessoa):
    def trabalhar(self):
        print("O cozinheiro esta cozinhando")

prof = Professor()

prof.correr()
prof.trabalhar()