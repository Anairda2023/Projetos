x = float(input("Digite o primeiro número:"))
y = float(input("Digite o segundo número: "))
z = float(input("Digite o terceiro número:"))
if x > y and x > z:
    print(f"o maior número é o: {x}")
elif y > z and y > x:
    print(f"O maior número é o: {y}")
else:     
    print(f"O maior número é o: {z}")
    
