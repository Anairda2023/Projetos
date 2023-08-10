print("Você estuda em qual turno?")
turno = input("Digite M para manutino M, V para vespertino e N para noturno:  ")
turno = turno.upper()
if turno == "M":
    print("Bom Dia!!")
elif turno == "V":
    print("Boa Tarde!!")
elif turno == "N":
    print("Boa Noite!!")
else:
    print("Valor inválido")


