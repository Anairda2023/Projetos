class Conta:
#Atributos
    
    __agencia:int
    __numero: int
    __titular: str
    __saldo  = 0.0

#Contrutor
    def __init__(self, agencia: int, numero: int, titular:str):
        self.__agencia = agencia
        self.__numero = numero
        self.__titular = titular
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
        return self.__saldo
        
#Métodos
    def depositar(self, valor: float):
        self.__saldo += valor


    