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
    
class Circulo:
    def __init__(self, raio:float = 0, centro:Ponto2D = 0) -> None:
        self.raio = raio
        self.centro = centro
    
    @property
    def raio(self) -> float:
        return self.__raio
    
    @raio.setter
    def raio(self, novoRaio) -> None:
        self.__raio = novoRaio

    def inflar(self, valor:int) -> None:
        self.raio = (self.raio + valor)

    def desinflar(self, valor:int) -> None:
        self.raio = (self.raio - valor)

    def mover(self, novoPonto:Ponto2D = None) -> None:
        if novoPonto == None:
            novoPonto = Ponto2D(0, 0)

        self.centro = novoPonto

    def area(self) -> float:
        return f"Área: {round(3.1415 * self.raio * self.raio, 2)}"

    def __str__(self) -> str:
        return f"Raio: {self.__raio} Centro: {self.centro}"
    

p1 = Ponto2D(5, 5)
p2 = Ponto2D(7, 2)

c1 = Circulo(10, p1)
print(c1)

c1.inflar(5)
print(c1)

c1.desinflar(10)
print(c1)

c1.mover(p2)
print(c1)

print(c1.area())

