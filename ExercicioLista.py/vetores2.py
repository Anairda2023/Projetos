numeros = []
maior = 0

for n in range(5):
    numero = int(input(f"Digite o número {n+1}: "))
       
    numeros.append(numero)
#Você pega o que tem na lista e printa na ordem decrescente
numeros.sort(reverse=True)

maior = numeros[0]

print(f"O maior número da list {numeros} é {maior}")



