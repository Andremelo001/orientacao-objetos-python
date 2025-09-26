# Substituição de Liskov: diz que uma classe mãe pode ser substituida pela sua classe filho sem perder o sentido
# quebra
class Animal:
    def alimentar(self):
        print("O animal está se alimentando")

class Cachorro(Animal):
    def latir(self):
        print("O cachorro esta latindo")

class Peixe(Cachorro):
    def nadar(self):
        print("O prixe esta nadando")
    
    def latir(self):
        raise Exception("O peixe nao late")