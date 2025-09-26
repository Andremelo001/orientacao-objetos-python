# O principal ponto do principio da substituição de liskov é utilizar de heranças que fazem sentido

class ConnectionDB:
    def conectar(self):
        print("Conectando ao Banco")

class SqlRepository(ConnectionDB):
    def select(self):
        print("Buscando dados no banco SQL")

class NoSQLRepository(ConnectionDB):
    def select(self):
        print("Buscando dados no banco NoSQL")

class DBHandler(SqlRepository):
    def alterar_tabela(self):
        print("Alterando tabela em SQL")
