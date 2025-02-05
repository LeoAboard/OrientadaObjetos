class Ponto2D:
    def __init__(self, X:float = 0, Y:float = 0):
        self.X = X
        self.Y = Y

    @property
    def X(self) -> float:
        return self.__X
    
    @X.setter
    def X(self, novoX:float) -> None:
        self.__X = novoX

    @property
    def Y(self) -> float:
        return self.__Y
    
    @Y.setter
    def Y(self, novoY:float) -> None:
        self.__Y = novoY

    def compara(self, outrosPontos:'Ponto2D') -> bool:
        return self.__X == outrosPontos.__X and self.__Y == outrosPontos.__Y
    
    def __str__(self) -> str:
       return f"X:{self.__X} Y:{self.__Y}"
    
    def distancia(self, outrosPontos:'Ponto2D') -> 'Ponto2D':
        distancia = Ponto2D((self.__X - outrosPontos.__X), (self.__Y - outrosPontos.__Y))
        return f"Distância: {distancia}"

    def clone(self) -> 'Ponto2D':
        pontoClone = Ponto2D(self.__X, self.__Y)
        return pontoClone


p1 = Ponto2D(100, -110)
p2 = Ponto2D()                   #sem parametros, recebe o valor default
p3 = Ponto2D(100, -110)
p4 = Ponto2D(-500, -343)

print(p1)
print(p1.compara(p2))
print(p1.compara(p3))
print(p1.distancia(p4))
print(p1.clone())
