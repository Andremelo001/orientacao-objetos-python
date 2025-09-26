class Mamifero:
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao

    def andar(self) -> None:
        print(f"O animal esta andando pela cidade {self.localizacao}")

#Herança
#Cachorro herda todos os elementos publicos de Mamifero
class Cachorro(Mamifero):
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao) # se refere ao construtor da classe superior
    
    def latir(self) -> None:
        print("O animal está latindo")
        self.andar()


cachorro = Cachorro("xique-xique")

cachorro.latir()