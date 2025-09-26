class ClasseQualquer:
    def fazer(self) -> None:
        print("Estou fazendo algo")

class OutraCoisa(ClasseQualquer):
    def preparar(self) -> None:
        print("Estou preparando algo")
    
    #metodos iguais, porem com comportamentos diferentes
    def fazer(self) -> None:
        print("Estou fazendo outra coisa")

obj = ClasseQualquer()

obj2 = OutraCoisa()

obj.fazer()

obj2.fazer()

obj.fazer()