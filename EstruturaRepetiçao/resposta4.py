a = 80000
b = 200000
ano = 0
while a < b:
    a = a + a * 0.03
    b = b + b * 0.015
    ano += 1
print(f"O número de anos em que A população a ultrapassou a B foi: {ano}")        

