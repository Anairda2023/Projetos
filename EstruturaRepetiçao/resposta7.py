x = []
for y in range(5):
    numero = float(input(f"Digite o numero {y+1} número: "))
    x.append(numero)
print("Os números digitados foram:", x)

maximo = max(x)
print(f"O maior número é: {maximo}")