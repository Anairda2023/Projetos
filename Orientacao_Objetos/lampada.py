class Lampada():
    #Atributos (características)
    __potencia =0
    __tensao = 0
    __cor = "branca"
    __estado = False
    #Contrutor

    def __inti__(self, cor, tensao, potencia):
        self.__cor = cor
        self.__tensao = tensao
        self.__potencia = potencia

    #Métodos (funcionalidades)
    def ligar(self):
        self.__estado = True

    def  desligar(self):
        self.__estado = True  

    def get_tensao(self):
        return self.__tensao    
    
    def iluminar(self):
        pass