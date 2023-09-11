# Faça um programa que leia 5 números e informe o maior número.

numeros = []
maior = 0

for n in range(5):
    numero = int(input(f"Digite o número {n + 1}: "))
    numeros.append(numero)

numeros.sort(reverse=True)

maior = numeros[0]

print(f"O maior número da lista {numeros} é {maior}")
