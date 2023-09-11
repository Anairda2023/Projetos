class Pessoa:
    def __init__(self, nome = str, idade = int, peso = float, altura = float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self, anos):
            self.idade += anos
            if self.idade < 21:
                self.crescer(0.5 * anos)
    def engordar(self, quilos):
            self.peso += quilos
   
    def emagrecer(self, quilos):
            self.peso -= quilos
    def crescer(self, centimetros):
            self.altura += centimetros


    def imprimir_informacoes(self):
            print(f"Nome: {self.nome}")
            print(f"Idade: {self.idade} anos")
            print(f"Peso: {self.peso} kg")
            print(f"Altura: {self.altura} cm")

# Exemplo de uso da classe
pessoa1 = Pessoa("Adri", 49, 61, 157)
print("Dados da pessoa: " , pessoa1.imprimir_informacoes)

pessoa1.envelhecer(2)
pessoa1.engordar(5)
pessoa1.emagrecer(3)
pessoa1.crescer(2)

print("Após as mudanças:")
pessoa1.imprimir_informacoes()


