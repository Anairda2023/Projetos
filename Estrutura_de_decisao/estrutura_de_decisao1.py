vogais = ("a", "e", "i" , "o", "u" )
letra = input("Digite uma letra do alfabeto: ")
eh_vogal = letra == "a" or letra == "e" or letra == "i" or letra =="o" or  letra == "u"
if eh_vogal:
    print("Vogal")
else:
    print("Não é vogal")

