nome = input("Insira o nome: ")
if len(nome) > 3:
    print(f"O nome inserido foi correto: {nome}")
else:
    print("Error. O nome tem que ter mais de três caracteres.")
idade = int(input("Insira a idade: "))
if 0 <  idade <  150: 
    print("O valor da idade está correto")
else:
    print("Erro. Insira um valor válido entre 0 e 150")
salario = float(input("Insira o valor do salário: "))
if salario > 0:
     print(f"O salário é: {salario}")
else:
    print("Valor errado. O salário tem que ser maior que zero.")     
sexo = input("Insira F para sexo feminino e M para sexo masculino: ")
sexo = sexo.upper()
if sexo == "F":
    print("Sexo feminino.")
elif sexo == "M":
    print("Sexo masculino.")
else:
    print("Erro. Você só pode inserir  F para sexo feminino e M para sexo masculino")    
estadocivil = input("Insira C para casado, S para separado, V para viúvo e D para divorciado.")
estadocivil = estadocivil.upper()
if estadocivil == "C":
    print("Estado civil casado")
elif estadocivil == "S":
    print("Estado civil separado")
elif estadocivil == "V":
    print("Estado civil viúvo")
elif estadocivil == "D":
    print("Estado civil divorciado")
else:
    print("Erro. Você só pode inserir C para casado, S para separado, V para viúvo e D para divorciado.")    

