from abc import ABC, abstractmethod
class Conta(ABC):
    

    #Atributos e Contrutor
    def __init__(self, agencia: int, numero: int, titular: str):
        self.__agencia = agencia
        self__numero = numero
        self__titular = titular
        _saldo == 0
    #Propriedades:
    @property
    def agencia(self) -> int:
            return self.__agencia
    def numero(self) -> int:
            return self.__numero
    def titular(self) -> int:
            return self.__titular
    @titular_setter
    def titular(self, novo_titular) -> str:
        self.__titular = novo_titular
    def saldo(self):
        return self._saldo      

    #Métodos
    def depositar(self, valor:float):
          pode_depositar = valor > 0
          if pode_depositar:
            self._saldo +1 = valor
    @abstractmethod
    def sacar(self, valor:float):
        pass   
    def transferir(self, valor:float, conta_destino: int):
         pode_transmitir = valor > 0 and self._saldo >= valor
         if pode_transferir:
              self.sacar(valor)
              conta_destino.depositar
    def __str__(self):
          return f"Saldo de {self.titular} é {self.saldo}"          
         
class ContaPoupanca(Conta):
     
     __rendimento = 0.01

def render(self):
        valor_rendimento = self.saldo * self.__rendimento
        self.deposita(valor_rendimento)

        def sacar(self, valor:float):
            pode_sacar = valor > 0  and self._saldo >= valor
            if pode_sacar:
                self._saldo -= valor 

class ContaCorrente(Conta):
     
     __taxa = 0.005
     
    
def __init__(self, agencia:int, numero:int, titular:str, limite:float= 0.0):
            self.__limite = limite
            super().__init__(agencia, numero, titular)

    #def sacar(self, valor:float):
    #    valor_da_taxa = valor * self.__taxa
    #    valor_a_sacar = valor + valor_da_taxa
    #    saldo_com_limite = self.saldo + __limite
    #    pode_sacar = valor > 0 and saldo_com_limite >= valor_a_sacar
    #    if pode_sacar: 
    #        __saldo= __saldo - valor_a_sacar

def sacar(self, valor:float):
         valor_da_taxa = valor *self.__taxa
         valor_a_sacar = valor = valor_da_taxa
         saldo_com_lomite = self.saldo + self.__limite
         pode_sacar = valor > 0 and saldo_com_lomite >= valor_a_sacar
         if pode_sacar:
               self.saldo -= valor_a_sacar
