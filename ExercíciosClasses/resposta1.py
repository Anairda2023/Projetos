class Bola():
    #Atributos
    __cor = str
    __circunferencia = float
    __material = str

    #Contrutor

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        
    def trocaCor(self, nova_cor):
        self.cor = nova_cor
        
    def mostraCor(self):
        return self.cor

    # Criando uma instância da classe Bola
    minha_bola = Bola(cor="amarela", circunferencia=10, material="plástico")

    print("Cor da bola:", minha_bola.mostraCor())  # Deve imprimir "azul"

    minha_bola.trocaCor("vermelho")
    print("Nova cor da bola:", minha_bola.mostraCor())  # Deve imprimir "vermelho"
