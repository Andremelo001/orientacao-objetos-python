class Pessoa:
    def __init__(self, nome: str):
        self.altura = 1.72
        self.idade = 10
        self.nome = nome

    def correr(self):
        print(f"Meu nome é {self.nome}, eu corro devagar pois tenho {self.altura} de altura")

    def comer(self):
        print(f"Eu tenho que comer muito, pois estou com {self.idade} anos de idade, na fase de crescimento")
    
pessoa = Pessoa("André")

pessoa.comer()

pessoa.correr()

