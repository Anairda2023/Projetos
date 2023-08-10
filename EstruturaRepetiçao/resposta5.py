a = int(input("Digite o número da população A: "))
b = int(input("Digite o número da população B: "))
txa = float(input("Digite a taxa de crescimento em percentuais da população A: "))
txb = float(input("Digite a taxa de crescimento em percentuais da população B: "))
txa = txa /100
txb = txb / 100
ano = 0
while a < b:
    a = a + a * txa
    b = b + b * txb
    ano += 1
print(f"O número de anos em que A população a ultrapassou a B foi: {ano}")        

