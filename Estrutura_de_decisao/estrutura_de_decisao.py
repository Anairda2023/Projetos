# Você cria uma variável e chama de pi = 3.14 ou baixa a biblioteca do math
# O sinal de igual em python é ==
# != diferente de
nota1 = float(input("Digite a nota 1: "))
nota_invalida = nota1 < 0 or nota1 > 10
while nota_invalida:
    print("A nota tem que ser entre 0 e 10")
    nota1 = float(input("Digite a nota 1:"))
    nota_invalida = nota1 < 0  or nota1 >10
    
nota2 = float(input("Digite a nota 2: "))
nota_invalida = nota2 < 0  or nota2 >10
while nota_invalida:
    print("A nota tem que ser entre 0 e 10")
    nota2 = float(input("Digite a nota 2:"))
    nota_invalida = nota2 < 0  or nota2 >10
    
nota3 = float(input("Digite a nota 3: "))
nota_invalida = nota3 < 0  or nota3 >10
while nota_invalida:
    print("A nota tem que ser entre 0 e 10")
    nota3 = float(input("Digite a nota 3:"))
    nota_invalida = nota3 < 0  or nota3 >10
    
nota_invalida = nota3 < 0  or nota3 >10    
media = ((nota1 * 4 + nota2 * 5 + nota3 * 6) / 15)
aprovado = media >= 7
recuperacao = media > 3 and media < 7
reprovado = media < 3 
if aprovado:
    print(f"Parabéns! Você está APROVADO com a média {media}! \o/")
elif recuperacao:
    print(f"Quase! Você está em recuperação com a média: {media}")
    w = float(input("Insira a quarta_nota: "))
    nova_media = (media + w) / 2
    aprovado = nova_media >= 5
    if aprovado:
        print (f"Parabens! Você está aprovado com a média: {media}")
    else:
        print (f"Que pena! Você está reprovado com média {media}! :(")   
elif reprovado:
    print(f"Que pena! Você está REPROVADO com média {media} :(") 

