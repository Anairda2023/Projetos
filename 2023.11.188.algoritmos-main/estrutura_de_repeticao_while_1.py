nota1 = float(input("Digite a nota 1:\n"))

nota_invalida = nota1 < 0 or nota1 > 10
while nota_invalida:
    print("A nota deve ser entre 0 (zero) e 10 (dez)")
    nota1 = float(input("Digite a nota 1:\n"))
    nota_invalida = nota1 < 0 or nota1 > 10

print(f"Nota valida: {nota1}")
