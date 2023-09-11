from funcoes import inss, somar
from classes.pessoa import Pessoa

# salario = float(input("Valor do salario: "))
# print(f"O desconto será de {inss(salario)}")

joao = Pessoa("João Victor", 24)
sergio = Pessoa("Sergio", 35)

print(f"O nome é {joao.nome} com idade {joao.idade}")
print(f"O nome é {sergio.nome} com idade {sergio.idade}")
