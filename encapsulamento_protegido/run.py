class Mamifero:
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao
        self._tamanho = 1.23

    def andar(self) -> None:
        print(f"O animal esta andando pelo {self.localizacao}")
    
    #Método protegido
    #Pode ser acessado dentro da propria classe e tambem dentro de classes filhas
    def _dormir(self) -> None:
        print("o animal esta dormindo")

class Cachorro(Mamifero):
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao) # se refere ao construtor da classe superior
    
    def latir(self) -> None:
        print("O animal está latindo")
        self.andar()
        self._dormir()
        print(self._tamanho)

dog = Cachorro("Brasil")

dog.latir()


# deveria retornar erro, elementos protegidos não podem ser chamados por objetos
# mas em python pode :)
# mas é uma convençao ao utilizar o _ na frente de um método, nao chama-lo por objetos
# dog._dormir()
# print(dog._tamanho)