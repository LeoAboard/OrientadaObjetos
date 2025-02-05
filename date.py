class data:
    def __init__(self, dia:int, mes:int, ano:int):
        self.ano = ano
        self.mes = mes
        self.dia = dia

    @property
    def dia(self) -> int:
        return self.__dia
    
    @dia.setter
    def dia(self, novoDia) -> None:
        mes = self.__mes
        ano = self.__ano

        if(novoDia <= 31 and novoDia >= 1):
            if(novoDia == 31):
                if((mes <= 7 and mes%2 == 1)):
                    self.__dia = 31
                elif((mes > 7 and mes%2 == 0)):
                    self.__dia = 31
                else:
                    self.__dia = 30
                    
            if (novoDia > 28 and mes == 2):
                if(ano%4  == 0):
                    self.__dia = 29
                else:
                    self.__dia = 28

            else:
                self.__dia = novoDia
        else:
            self.__dia = 1
    
    @property
    def mes(self) -> int:
        return self.__mes
    
    @mes.setter
    def mes(self, novoMes) -> None:
        if(novoMes < 1):
            self.__mes = 1
        elif(novoMes > 12):
            self.__mes = 12
        else:
            self.__mes = novoMes

    @property
    def ano(self) -> int:
        return self.__ano
    
    @ano.setter
    def ano(self, novoAno) -> None:
        if(novoAno >= 1):
            self.__ano = novoAno
        else:
            self.__ano = 1

    def __str__(self) -> str:
        return f"{self.__dia:02}/{self.__mes:02}/{self.__ano:04}"
    
    def proximo(self) -> str:
        if (self.__dia >= 28) and (self.__mes == 2):
                if(self.__dia == 28 and self.__ano%4 == 0):
                    self.__dia = 29
                else:
                    self.__mes = 3
                    self.__dia = 1

        elif self.__dia == 31:
            if self.__mes == 12:
                self.__ano = (self.__ano + 1)
                self.__mes = 1
                self.__dia = 1
            else:
                self.__mes = (self.__mes + 1)
                self.__dia = 1

        elif (self.__dia == 30) and ((self.__mes <= 7 and self.__mes%2 == 0) or (self.__mes > 7 and self.__mes%2 == 1)):
            self.__mes = (self.__mes + 1)
            self.__dia = 1

        else:
            self.__dia = (self.__dia + 1)

        data.__str__(d1)


d1 = data(29, 2, 2025)
print(d1)

d1.proximo()
print(d1)
