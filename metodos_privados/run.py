class Pessoa:
    def __init__(self, altura: int, cpf: str) -> None:
        self.altura = altura

        # atributo privado - so pode ser acessado dentro da classe
        self.__cpf = cpf

    def apresentar(self):
        print(f"Ola!, Minha altura - {self.altura}")
        self.__coletar_documento()

    # Método privado - so pode ser acessado dentro da classe
    def __coletar_documento(self):
        print(f"Meu documento - {self.__cpf}")


andre = Pessoa(1.72, "582523959023")

# Erro - metodo privado esta sendo chamado fora da classe
# andre.__coletar_documento()

# Erro - atributo privado esta sendo chamado fora da classe
#print(andre.__cpf)

andre.apresentar()