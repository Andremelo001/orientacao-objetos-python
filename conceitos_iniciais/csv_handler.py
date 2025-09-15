class CsvHandler:
    def __init__(self, diretory) -> None:
        self.dir = diretory
    
    def insert_data_in_csv(self, data):
        print(f"Inserindo {data} em {self.dir}")

    def read_data(self):
        print(f"read data in {self.dir}")

csv_handle = CsvHandler("o/caminho/do/diretorio/.csv")

#csv_handle.insert_data_in_csv("novo valor no diretorio")

csv_handle.read_data()