class Artista:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo
    
    def apresentar_show(self) -> None:
        print(f"O {self.tipo} está apresentando o seu show")

class Circo:
    def apresentar(self, artista: Artista) -> None:
        print("O circo está abrindo")
        artista.apresentar_show()
        print("O publico aplaude")
    

artista = Artista("Palhaço")

circo = Circo()

circo.apresentar(artista)