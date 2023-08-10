x = []
for y in range(5):
    numero = float(input(f"Digite o numero {y+1} número: "))
    x.append(numero)
soma = sum(x)
media = soma / len(x)
print(f"A soma foi: {soma}")
print(f"A média foi: {media}")

