nota1 = float(input("Digite a nota 1:\n"))
nota_invalida = nota1 < 0 or nota1 > 10
while nota_invalida:
    print("A nota deve ser entre 0 (zero) e 10 (dez)")
    nota1 = float(input("Digite a nota 1:\n"))
    nota_invalida = nota1 < 0 or nota1 > 10

nota2 = float(input("Digite a nota 2:\n"))
nota_invalida = nota2 < 0 or nota2 > 10
while nota_invalida:
    print("A nota deve ser entre 0 (zero) e 10 (dez)")
    nota2 = float(input("Digite a nota 2:\n"))
    nota_invalida = nota2 < 0 or nota2 > 10

nota3 = float(input("Digite a nota 3:\n"))
nota_invalida = nota3 < 0 or nota3 > 10
while nota_invalida:
    print("A nota deve ser entre 0 (zero) e 10 (dez)")
    nota3 = float(input("Digite a nota 3:\n"))
    nota_invalida = nota3 < 0 or nota3 > 10

media = (nota1 * 4 + nota2 * 5 + nota3 * 6) / 15

aprovado = media >= 7
recuperacao = media > 3 and media < 7
reprovado = media < 3

if aprovado:
    print(f"Parabéns! Você está APROVADO com média {media}! \o/")
elif recuperacao:
    print(f"Quase! Você está RECUPERAÇÃO com média {media}! :|")
    nota4 = float(input("Digite a nota 4:\n"))
    media = (media + nota4) / 2
    aprovado = media >= 5
    if aprovado:
        print(f"Parabéns! Você está APROVADO com média {media}! \o/")
    else:
        print(f"Que pena! Você está REPROVADO com média {media}! :(")
elif reprovado:
    print(f"Que pena! Você está REPROVADO com média {media}! :(")
