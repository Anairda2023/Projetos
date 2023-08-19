#from funcao import inss
from classes.pessoa import Pessoa

#salario = float(input("Digite seu salário: "))
#print(f"o desconto será de: {salario}")

joao = Pessoa("João Victor", 24)
joao.nome = "João Victor"
joao.idade = 24

print(f"O nome é {joao.nome} com idade {joao.idade}")

