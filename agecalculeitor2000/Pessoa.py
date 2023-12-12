from datetime import datetime as dt

class Pessoa:
    
    def __init__(self,nome: str, dataNacimento: dt) -> None:
        self.__nome = nome
        self.__dataNacimento = dataNacimento
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.nome = nome
    
    @property
    def dataNacimento(self):
        return self.__dataNacimento
    
    @dataNacimento.setter
    def dataNacimento(self, dataNacimento: dt):
        self.dataNacimento = dataNacimento
        
    
    def idade(self):
        hoje = dt.today()
        return hoje.year - self.__dataNacimento
        
        