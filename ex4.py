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
    
class retangulo:
    def __init__(self, largura:int, altura:int, pontos:Ponto2D):  #pontos representam o canto inferior esquerdo
        self.largura = abs(largura)
        self.altura = abs(altura)
        self.pontos = pontos

    @property
    def largura(self) -> int:
        return self.__largura
    
    @largura.setter
    def largura(self, novaLargura:int) -> None:
        self.__largura = novaLargura

    @property
    def altura(self) -> int:
        return self.__altura
    
    @altura.setter
    def altura(self, novaAltura:int) -> None:
        self.__altura = novaAltura

    def mover(self, novoPonto:Ponto2D = None) -> None:
        if novoPonto == None:
            novoPonto = Ponto2D(0,0)

        self.pontos = novoPonto

    def area(self) -> int:
        return self.altura * self.largura
    
    def interseccao(self, r2:'retangulo') -> bool:
        area = self.area()
        if (self.pontos.X + self.largura < r2.pontos.X) or (r2.pontos.X + r2.largura < self.pontos.X) or (self.pontos.Y + self.altura < r2.pontos.Y) or (r2.pontos.Y + r2.altura < self.pontos.Y):
            return False
        else:
            return True

    def __str__(self) -> str:
        return f"Altura: {self.altura}\nLargura: {self.largura}\nPontos: {self.pontos}"
    

p1 = Ponto2D(2, 3)
p2 = Ponto2D(2, 1)
r1 = retangulo(3, 2, p1)
r2 = retangulo(3, 2, p2)


print(r1)
print(r1.area())
print(r1.interseccao(r2))

