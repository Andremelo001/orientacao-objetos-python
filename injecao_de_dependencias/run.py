class Celular:
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo

    def enviar_mensagem(self, mensagem: str) -> None:
        print(f"Enviando a mensagem: {mensagem}")
    
    def abrir_emails(self) -> None:
        print("Abrindo os emails.......")
    
    def abrir_youtube(self) -> None:
        print("Abrindo o youtube.......")

class Pessoa:
    def __init__(self, celular: Celular) -> None:
        #usar dependencias privadas
        self.__celular = celular
    
    def pedir_pizza(self) -> None:
        print("Buscando o celular...")
        print("Definindo o sabor")
        self.__celular.enviar_mensagem("quero uma de calabresa")
        print("aguardando a chegada da pizza")
    
    def estudar(self) -> None:
        print("sentando num computador")
        self.__celular.abrir_youtube()
        print("Anotando o conteudo")


android = Celular("samsung")
ios = Celular("iphone")

pessoa = Pessoa(android)

pessoa.pedir_pizza()