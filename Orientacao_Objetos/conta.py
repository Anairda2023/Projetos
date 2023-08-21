class Conta:
    #Atributos
    __agencia: int
    __numero: int
    __titular: str
    __saldo == 0

    #Contrutor
    def __init__(self, agencia: int, numero: int, titular: str):
        self.__agencia = agencia
        self__numero = numero
        self__titular = titular
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
        return self.__saldo      

    #Métodos
    def depositar(self, valor:float):
          pode_depositar = valor > 0
          if pode_deposita :
            self.__depositar +1 = valor

    def sacar(self, valor:float):
        pode_sacar = valor > 0 and self.__saldo >= valor
        if pode_sacar: 
            self.__sacar -1 = valor     
    def transferir(self, valor:float, conta_destino: int):
         pode_transmitir = valor > 0 and self.__saldo >= valor
         if pode_transferir:
              self.sacar(valor)
              conta_destino.depositar
         
         
                