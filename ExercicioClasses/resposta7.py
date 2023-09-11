class Tamagushi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
    def alterar_fome(self, valor_fome):
        if 0 <= valor_fome <= 100:
            self.fome = valor_fome
        else:
            print("Valor de fome inválido. Deve estar entre 0 e 100.")

    def alterar_saude(self, valor_saude):
        if 0 <= valor_saude <= 100:
            self.saude = valor_saude
        else:
            print("Valor de saúde inválido. Deve estar entre 0 e 100.")
    
    def alterar_idade(self, anos):
        if anos >= 0:
            self.idade += anos
        else:
            print("Valor de idade inválido. Deve ser maior ou igual a zero.")

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def calcular_humor(self):
        return (self.fome + self.saude) / 2

    def imprimir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Fome: {self.fome}")
        print(f"Saúde: {self.saude}")
        print(f"Idade: {self.idade}")
        print(f"Humor: {self.calcular_humor()}")

# Exemplo de uso da classe
bichinho = Tamagushi("Tama")

bichinho.alterar_fome(50)
bichinho.alterar_saude(80)
bichinho.alterar_idade(2)

bichinho.imprimir_informacoes()
