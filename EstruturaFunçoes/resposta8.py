def contar_digitos(numero):
    numero = str(numero)
    nn = len(numero)
    return nn
# Solicita o número ao usuário
num = int(input("Digite um número inteiro: "))
quantidade_digitos = contar_digitos(num)

print(f"O número {num} tem {quantidade_digitos} dígitos.")