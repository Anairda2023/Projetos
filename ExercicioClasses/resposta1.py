class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, novacor):
        self.cor = novacor
    def mostra_cor(self):
        return self.cor
definicao_de_bola = Bola("azul", 60, "plático" )

print("A cor da bola é: ", definicao_de_bola.mostra_cor())

definicao_de_bola.troca_cor("branca")

print("A nova cor da bola é: ", definicao_de_bola.mostra_cor())


