x = input("Digite uma letra:")
x = x.lower()
if x in "aeiou":
    print("A letra digitada é uma vogal")
elif x.isalpha():
    print("A letra digitada é uma consoante")
else:
    print ("A letra digitada é um caractere inválido")
