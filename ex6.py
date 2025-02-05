class contaCorrente:
    def __init__(self, numero:int, titular:str, saldo:float, limite:float):
        self.numero = numero
        self.titular = titular
        self.saldo = abs(saldo)
        self.limite = abs(limite)

    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, novoNumero:int) -> None:
        self.__numero = novoNumero

    @property
    def titular(self) -> str:
        return self.__titular

    @titular.setter
    def titular(self, novoTitular:str) -> None:
        self.__titular = novoTitular

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, novoSaldo:float) -> None:
        self.__saldo = novoSaldo

    @property
    def limite(self) -> float:
        return self.__limite

    @limite.setter
    def limite(self, novoLimite:float) -> None:
        self.__limite = novoLimite

    def depositar(self, valor:float) -> None:
        if valor > 0:
            self.saldo = self.saldo + valor
    
    def sacar(self, valor:float) -> None:
        if (valor > 0) and (valor <= self.saldo) and (valor <= self.limite):
            self.saldo = self.saldo - valor

    def transferir(self, conta2:'contaCorrente', valor:float) -> None:
        if (valor > 0) and (self.saldo >= valor):
            self.saldo = self.saldo - valor
            conta2.saldo = conta2.saldo + valor

    def __str__(self) -> str:
        return f"Conta: {self.numero}\nTitular: {self.titular}\nSaldo: {self.saldo}\nLimite de saque: {self.limite}"
    

    
conta1 = contaCorrente(1234, "Leonardo", 1600.50, 500)
conta2 = contaCorrente(5678, "Fulano", 2500.99, 799.99)

conta1.depositar(200.99)
print(conta1)

conta1.sacar(350.50)
print(conta1)

conta1.transferir(conta2, 400)
print(conta2)
    