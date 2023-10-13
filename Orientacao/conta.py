
from abc import ABC, abstractmethod
class Conta(ABC):

# Atributos e Contrutor
    def __init__(self, agencia: int, numero: int, titular:str):
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
        self._saldo = 0.0
#Propriedades
    @property
    def agencia(self) -> int:
        return self.__agencia
    @property
    def numero(self) -> int:
        return self.__numero
    @property
    def titular(self) -> str:
        return self.__titular
    
    @titular.setter
    def titular(self, novo_titular):
        self.__titular = novo_titular
    @property
    def saldo(self) -> float:
        return self._saldo
        
#Métodos
    def depositar(self, valor: float):
        pode_depositar = valor > 0
        if pode_depositar:
            self._saldo += valor

    @abstractmethod    
    def sacar(self, valor: float):
        pass
        
    def transferir(self, valor: float, conta_destino):
        pode_transferir = valor > 0 and self._saldo >= valor
        if pode_transferir:
            self.sacar(valor)
            conta_destino.depositar(valor)
    def _str_(self) -> str:
        return f"Saldo de {self.titular} é {self.saldo}"        

class ContaPoupanca(Conta):
    __rendimento = 0.01

    def render(self):
        valor_rendimento = self.saldo * self.__rendimento
        self.depositar(valor_rendimento)
    
    def sacar(self, valor: float):
        pode_sacar = valor > 0 and self._saldo >= valor
        if pode_sacar:
            self._saldo -= valor


class ContaCorrente(Conta):
#Taxa em 0.5 % todas as movimentações que retirem dinheiro
    __taxa = 0.005
    #Adicionar o cheque especial na conta corrente
    
    def __init__(self, agencia:int, numero:int, titular:str, limite:float = 0.0):
        self.__limite = limite
        super().__init__(agencia, numero, titular)
   

    #def sacar(self, valor:float):
    #    valor_da_taxa = valor * self.__taxa
    #    valor_a_sacar = valor + valor_da_taxa
    #    pode_sacar = valor > 0 and self.saldo >= valor_a_sacar
    #    if pode_sacar:
    #        super().sacar(valor_a_sacar)
    
    def sacar(self, valor: float):
        valor_da_taxa = valor * self.__taxa
        valor_a_sacar = valor + valor_da_taxa
        saldo_com_limite = self.saldo + self.__limite
        pode_sacar = valor > 0 and saldo_com_limite >= valor_a_sacar
        if pode_sacar:
            self._saldo -= valor_a_sacar

    