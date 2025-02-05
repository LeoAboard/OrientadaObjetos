class relogio:
    def __init__(self, h:int, m:int, s:int):
        self.h = h
        self.m = m
        self.s = s

    @property
    def h(self) -> int:
        return self.__h
    
    @h.setter
    def h(self, novaH) -> None:
        if novaH > 24 or novaH < 0:
            print("Horário inválido")
            exit()
        else:
            self.__h = novaH

    @property
    def m(self) -> int:
        return self.__m
    
    @m.setter
    def m(self, novoM) -> None:
        if novoM > 59 or novoM < 0:
            print("Horário inválido")
            exit()
        else:
            self.__m = novoM

    @property
    def s(self) -> int:
        return self.__s
    
    @s.setter
    def s(self, novoS) -> None:
        if novoS > 59 or novoS < 0:
            print("Horário inválido")
            exit()
        else:
            self.__s = novoS

    def __add__(self, r2:'relogio') -> 'relogio':
        s3 = self.s + r2.s
        m3 = self.m + r2.m
        h3 = self.h + r2.h

        if s3 > 59:
            s3 = s3 - 60
            m3 += 1

        if m3 > 59:
            m3 = m3 - 60
            h3 += 1

        if h3 > 24:
            h3 = h3 - 24

        r3 = relogio(h3, m3, s3)
        return r3
    
    def __sub__(self, r2:'relogio') -> 'relogio':
        if (self.h < r2.h) or ((self.h == r2.h) and (self.m < r2.m)) or (((self.h == r2.h) and (self.m == r2.m)) and (self.s < r2.s)):
            print("Primeiro horário deve ser maior que o segundo")
            exit()

        s3 = self.s - r2.s
        m3 = self.m - r2.m
        h3 = self.h - r2.h    

        if s3 < 0:
            s3 = s3 + 60
            m3 -= 1
        
        if m3 < 0:
            m3 = m3 + 60
            h3 = h3 - 1
        
        if h3 < 0:
            h3 = h3 + 24

        r3 = relogio(h3, m3, s3)
        return r3
    
    def __eq__(self, r2:'relogio') -> bool:
        if (self.h == r2.h) and (self.m == r2.m) and (self.s == r2.s):
            return True
        else:
            return False

    def __gt__(self, r2:'relogio') -> bool:
        if (self.h > r2.h) or ((self.h == r2.h) and (self.m > r2.m)) or (((self.h == r2.h) and (self.m == r2.m)) and (self.s > r2.s)):
            return True
        else:
            return False

    def __lt__(self, r2:'relogio') -> bool:
        if (self.h < r2.h) or ((self.h == r2.h) and (self.m < r2.m)) or (((self.h == r2.h) and (self.m == r2.m)) and (self.s < r2.s)):
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

    
r1 = relogio(20,0,30)
r2 = relogio(14, 38, 2)

r3 = r1 + r2
print(r3)

r4 = r2 - r3
print(r4)

print(r3 > r4)
print(r1 < r2)
print(r4 == r4)
    