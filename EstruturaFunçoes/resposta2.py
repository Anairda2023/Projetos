def imprimir_padrao(n):
    for i in range(1, n + 1):
        linha = '   '.join([str(j) for j in range(1, i + 1)])  # Cria a linha com os números de 1 a i
        print(linha)

# Solicita o valor de n ao usuário
n = int(input("Digite um valor inteiro para n: "))
imprimir_padrao(n)