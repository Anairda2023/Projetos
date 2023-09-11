class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.estomago = []

    def comer(self, alimento):
        self.estomago.append(alimento)
        print(f"{self.nome} comeu {alimento}.")

    def ver_estomago(self):
        if self.estomago:
            print(f"{self.nome} tem no estômago: {', '.join(self.estomago)}")
        else:
            print(f"{self.nome} está com o estômago vazio.")

    def digerir(self):
        if self.estomago:
            print(f"{self.nome} está digerindo {', '.join(self.estomago)}.")
            self.bucho = []
        else:
            print(f"{self.nome} não tem nada para digerir.")

# Criar dois macacos
macaco1 = Macaco("M1")
macaco2 = Macaco("M2")

# Alimentar os macacos
macaco1.comer("banana")
macaco2.comer("maçã")
macaco1.comer("laranja")

# Verificar o conteúdo do estômago
macaco1.ver_estomago()
macaco2.ver_estomago()

# Digerir
macaco1.digerir()
macaco2.digerir()

# Verificar o conteúdo do estômago após a digestão
macaco1.ver_estomago()
macaco2.ver_estomago()



