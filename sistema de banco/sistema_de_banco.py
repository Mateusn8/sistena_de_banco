class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valor):
        self.nome = valor

    @property 
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, valor):
        self.idade = valor

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None
    
    def inserirconta(self, conta):
        self.conta = conta

from abc import ABC, abstractmethod

class Conta(ABC): 
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    def detalhes(self):
        return f'agencia: {self.agencia}\nconta: {self.conta}\nsaldo: R${self.saldo}'
    
    def deposito(self, valor):
        self.saldo += valor
        self.detalhes()
        return 'valor depositado'
    
    @abstractmethod
    def sacar (self, valor):
        ...
    
class Contapoupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            return 'saldo insuficiente para sacar'
        else:
            self.saldo -= valor
            self.detalhes()
            return 'retire as notas'

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    
    def sacar(self,valor):
        if valor > (self.saldo + self.limite):
            return 'Saldo insuficiente para sacar'
        else:
            self.saldo -= valor
            self.detalhes()
            return 'retire as notas'

class Banco:
    def __init__(self):
        self.agencia = [4561, 8529, 0000]
        self.contas = [100, 120, 101]
        self.clientes = []

    def inserircliente(self, cliente):
        self.clientes.append(cliente)

    def autentificar(self, cliente, numerodaconta):
            
        if cliente not in self.clientes:
            return False
        
        if numerodaconta.conta not in self.contas:
            return False
        
        if cliente.conta.agencia not in self.agencia:
            return False
        
        else:
            return True
