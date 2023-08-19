class Lampada():

    #Atributos (características)

    #Para colocar em privado os atributos você coloca dois underlines - você está capsulando os atributos. Ninguém está vendo
    __potencia = 0
    __tensao = 0
    __cor ="branca"
    __estado = False



    #Contrutor
    def __init__(self, cor, potencia, tensao):
        self.__cor = cor
        self.__potencia = potencia
        self.__tensao = tensao

    #Métodos (funcionalidade)
    @property
    def potencia(self):
        return self.__potencia
    
    #o raise é uma exceção
    @potencia.setter
    def potencia(self, nova_potencia):
        if nova_potencia > 0:
            self.__potencia = nova_potencia
        else:
            raise TypeError("Não pode valores negativos")

    def get_tensao(self):
        return self.__tensao
 
    def get_cor(self):
        return self.__cor
 
    def get_estado(self):
        return self.__estado
 
    def ligar(self):
       self.__estado = True

    def desligar(self):
        self.__estado = True
 

    def iluminar(self):
        pass

    def aquecer (self):
        pass

    
    
    


