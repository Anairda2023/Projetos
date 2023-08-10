x = float(input("Insira o primeiro número: "))
y = float(input("Insira o segundo número: "))
z = float(input("Insira o terceiro número: "))
if x > y and x > z and y > z:
    print(f"Os números em ordem crescente são: {z} , {y} e {x}")
elif x > y and x > z and z > y:
    print(f"Os números em ordem crescente são: {y} , {z} e {x}")
elif y > x and y > z and z > x:
    print(f"Os números em ordem crescente são: {x} , {z} e {y}")
elif y > x and y > z and x > z:
    print(f"Os números em ordem crescente são: {z} , {x} e {y}")
elif z > x and z > x and y > x:
    print(f"Os números em ordem crescente são: {x} , {y} e {z}")
else:
    print(f"Os números em ordem crescente são: {y} , {x} e {z}")