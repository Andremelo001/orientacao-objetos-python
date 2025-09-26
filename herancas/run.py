class Mamifero:
    def __init__(self) -> None:
        self.localizacao = "brasil"

    def andar(self) -> None:
        print(f"O animal esta andando pelo {self.localizacao}")

#Herança
#Cachorro herda todos os elementos publicos de Mamifero
class Cachorro(Mamifero):
    
    def latir(self) -> None:
        print("O animal está latindo")
        self.andar()

mamifero = Mamifero()

mamifero.andar()

dog = Cachorro()

dog.andar()
valor = dog.localizacao