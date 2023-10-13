vogais = ("a", "e", "i" , "o", "u" )
letra = input("Digite uma letra do alfabeto: ")
eh_vogal = letra.lower() in vogais
if eh_vogal:
    print("Vogal")
else:
    print("Não é vogal")
