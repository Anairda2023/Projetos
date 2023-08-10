x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
z = float(input("Digite o terceiro número: "))
if x > y and x > z and y > z:
    print(f"O maior numero é o: {x} e o menor número é o: {z}")
elif x > y and x > z and z > y:
    print(f"O maior numero é o: {x} e o menor número é o: {y}")
elif y > x and y > z and x > z:
    print(f"O maior numero é o: {y} e o menor número é o: {z}")
elif y > x and y > z and z > x:
    print(f"O maior numero é o: {y} e o menor número é o: {x}")
elif z > x and z > y and y > x:
    print(f"O maior numero é o: {z} e o menor número é o: {x}")    
else:
    print(f"O maior numero é o: {z} e o menor número é o: {y}")   

