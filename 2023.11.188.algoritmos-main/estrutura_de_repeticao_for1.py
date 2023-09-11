# criar um programa que gere a tabuada de:
numero = int(input("Informe numero da tabuada que deseja:\n"))

numeros = range(1, 11)

print(f"======Tabuada de {numero}=======")

for n in numeros:
    print(f"{numero}\tx\t{n}\t=\t{numero * n}")

print(f"================================")
