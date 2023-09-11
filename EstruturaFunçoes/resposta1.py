def imprimir_padrao(n):
    for i in range(1, n + 1):
        linha = '   '.join([str(i)] * i)  # Cria a linha com o número i repetido i vezes
        print(linha)

# Solicita o valor de n ao usuário
n = int(input("Digite um valor inteiro para n: "))
imprimir_padrao(n)
