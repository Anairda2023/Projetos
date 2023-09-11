numero = []
def reverso_do_numero(numero):
    numero = str(numero)
    n = numero[::-1]  # Inverte a string
    return n
# Solicita o número ao usuário
num = int(input("Digite um número inteiro: "))
r = reverso_do_numero(num)

print(f"O reverso do número {num} é: {r}")


