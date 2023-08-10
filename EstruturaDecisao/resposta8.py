x = float(input("Qual o preço da banana: "))
y = float(input("Digite o preço da maçã: "))
z = float(input("Digite o preço da pera: "))
if x < y and x < z:
    print("Vou comprar a banana")
elif y < x and y < z:
     print("Vou comprar a maçã")
else:
     print("Vou comprar a pera")
     