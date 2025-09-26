class ConectorBD:
    def __init__(self) -> None:
        self.connection = None

    def conectar_ao_bd(self) -> None:
        self.connection = True

#manipulação de dados do BD
class RepositorioDB:
    def __init__(self, connection: ConectorBD) -> None:
        self.__conexao = connection
    
    def busca_dados(self) -> list:
        if self.__conexao.connection:
            return [1, 2, 3, 4]
        
        return None

class RegraDeNegocio:
    def __init__(self, repo: RepositorioDB):
        self.__repo = repo

    def calcular_resultados(self) -> None:
        dados = self.__repo.busca_dados()

        if not dados:
            print("Dados não encontrados")
        else:
            resposta = 0
            for dado in dados:
                resposta += dado
            print(f"O resultado é: {resposta}")

conn = ConectorBD()
conn.conectar_ao_bd()

repo = RepositorioDB(conn)

regra = RegraDeNegocio(repo)

regra.calcular_resultados()
    