class funcionario:
    def __init__(self, nome:str, CPF:str, salario:float, departamento:str):
        self.nome = nome
        self.CPF = CPF
        self.salario = salario
        self.departamento = departamento

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, novoNome) -> None:
        self.__nome = novoNome

    @property
    def CPF(self) -> str:
        return self.__CPF
    
    @CPF.setter
    def CPF(self, novoCPF) -> None:
        self.__CPF = novoCPF

    @property
    def salario(self) -> float:
        return self.__salario
    
    @salario.setter
    def salario(self, novoSalario) -> None:
        if novoSalario >= 0:
            self.__salario = novoSalario

    @property
    def departamento(self) -> str:
        return self.__departamento
    
    @departamento.setter
    def departamento(self, novoDepartamento) -> None:
        self.__departamento = novoDepartamento

    def __str__(self) -> str:
        return f"Nome: {self.nome}\nCPF: {self.CPF}\nSalário: {self.salario}\nDepartamento: {self.departamento}\n"

    def bonificar(self) -> None:
        self.salario = (self.salario + (self.salario * 0.10))


class gerente(funcionario):
    def __init__(self, senha:str, num_funcionarios:int, nome:str, CPF:str, salario:float, departamento:str):
        super().__init__(nome, CPF, salario, departamento)
        self.senha = senha
        self.num_funcionarios = num_funcionarios

    @property
    def senha(self) -> str:
        return self.__senha
    
    @senha.setter
    def senha(self, novaSenha) -> None:
        self.__senha = novaSenha

    @property
    def num_funcionarios(self) -> int:
        return self.__num_funcionarios

    @num_funcionarios.setter
    def num_funcionarios(self, novoNum_funcionarios) -> None:
        self.__num_funcionarios = novoNum_funcionarios

    def autenticar_senha(self, senhaInserida) -> bool:
        if senhaInserida == self.__senha:
            return True
        else:
            return False
        
    def bonificar(self) -> None:
        self.salario = (self.salario + (self.salario * 0.15))



f1 = funcionario("Mauricio", "123456789-10", 1200.00, "Finanças")
print(f1)

g1 = gerente(senha="123abc", num_funcionarios=10, nome="Eduardo", CPF="012.345.678-91", salario=7400.98, departamento="Finanças")
print(g1)

g1.bonificar()
print(g1)
f1.bonificar()
print(f1)

print(g1.autenticar_senha("456CBA"))
print(g1.autenticar_senha("123abc"))


