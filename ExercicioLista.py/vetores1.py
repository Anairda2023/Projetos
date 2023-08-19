numeros = []
maior = 0

for n in range(5):
    numero = int(input(f"Digite o número {n+1}: "))
    if n == 0:
        maior = numero
    elif numero > maior:
        maior = numero
    numeros.append(numero)
print(f"O maior número da list {numeros} é {maior}")

#para lista a lista de trás para frente é:
numeros.sort(reverse=True)

