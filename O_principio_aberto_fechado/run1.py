# Quebra o principio aberto e fechado, pois para adicionar uma nova funcionalidade(um novo show) é preciso alterar a classe circo
class Circo:
    def apresentar(self, command: int) -> None:
        if command == 1:
            self.__show_palhaco()
        if command == 2:
            self.__show_malabarista()
        if command == 3:
            self.__show_magico()

    def __show_palhaco(self):
        print("O palhaço está apresentando o show")
    
    def __show_malabarista(self):
        print("O malabarista está apresentando o show")

    def __show_magico(self):
        print("O Magico está apresentando o show")
    

circo = Circo()

command = 1
circo.apresentar(command)