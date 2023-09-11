
def somar_tres_numeros(a, b, c):
    soma = a + b + c
    return soma

# Solicita os valores ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

resultado = somar_tres_numeros(num1, num2, num3)
print("A soma dos três números é:", resultado)