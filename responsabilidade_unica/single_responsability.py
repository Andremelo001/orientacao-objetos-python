class SistemaCadastral:
    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validade_input(nome, idade):
            self.__register_user(nome, idade)
        else:
            self.__error_hadler()
            
    def __validade_input(self, nome: str, idade: int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int)
    
    def __register_user(self, nome: str, idade: int) -> None:
        print(f"Cadastrar usuario com nome {nome}, e idade {idade}")

    def __error_hadler(self) -> None:
        print("dados invalidos")

sistema = SistemaCadastral()

sistema.cadastrar("André", 20)

