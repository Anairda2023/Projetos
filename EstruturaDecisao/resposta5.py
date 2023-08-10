x = float(input("Digite a primeira nota: "))
y = float(input("Digite a segunda nota: "))
media = (x + y) / 2
if media == 10:
    print("Aprovado com distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

    