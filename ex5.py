class pais:
    def __init__(self, codigo:str, nome:str, populacao:int, dimensao:float):
        self.codigo = codigo
        self.nome = nome
        self.populacao = populacao
        self.dimensao = dimensao
        self.fronteiras = []

    @property
    def codigo(self) -> str:
        return self.__codigo
    
    @codigo.setter
    def codigo(self, novoCodigo:str) -> None:
        self.__codigo = novoCodigo

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, novoNome:str) -> None:
        self.__nome = novoNome

    @property
    def populacao(self) -> int:
        return self.__populacao
    
    @populacao.setter
    def populacao(self, novoPopulacao:int) -> None:
        self.__populacao = novoPopulacao

    @property
    def dimensao(self) -> float:
        return self.__dimensao
    
    @dimensao.setter
    def dimensao(self, novoDimensao:float) -> None:
        self.__dimensao = novoDimensao

    def add_fronteira(self, novaFronteira:'pais') -> None:
        if (pais != self) and pais not in self.fronteiras:
            self.fronteiras.append(novaFronteira)
            novaFronteira.fronteiras.append(self)

    def limitrofe(self, pais2:'pais'):
        if pais2 in self.fronteiras:
            return True
        else:
            return False
        
    def igualdade(self, pais2:'pais') -> bool:
        if(self.codigo == pais2.codigo):
            return True
        else:
            return False
        
    def densidade(self) -> float:
        return round((self.populacao / self.dimensao),2)
    
    def vizinhos(self, pais2:'pais') -> 'pais':
        vizinhos = set(self.fronteiras) & set(pais2.fronteiras)
        if vizinhos:
            print("Vizinhos comuns:")
            for pais in vizinhos:
                print(pais.nome)
        else:
            print("Nenhum vizinho comum")

    def __str__(self) -> str:
        return f"Nome: {self.nome}\nISO: {self.codigo}\nPopulação: {self.populacao} habitantes\nTerritório: {self.dimensao} km²"



brasil = pais("BRA", "Brasil", 216400000, 8510000)
argentina = pais("ARG", "Argentina", 473274097, 2780000)
paraguai = pais("PRY", "Paraguai", 6862000, 406752)
peru = pais("PER", "Peru", 34350000, 1285000)
alemanha = pais("DEU", "Alemanha", 84480000, 357592)
dinamarca = pais("DNK", "Dinamarca", 5947000, 42952)

brasil.add_fronteira(argentina)
brasil.add_fronteira(peru)
brasil.add_fronteira(paraguai)
argentina.add_fronteira(paraguai)
dinamarca.add_fronteira(alemanha)

print(brasil)
print(brasil.limitrofe(peru))
print(brasil.igualdade(brasil))
print(brasil.densidade())
brasil.vizinhos(paraguai)
        
    
    