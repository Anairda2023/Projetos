def bem_vindo():
    print("Bem Vindo!")

bem_vindo()
bem_vindo()
bem_vindo()

# Argumento são dados que você precisa informar para poder a função funcionar

def entrada(texto):
    return int(input(texto))
#####################

entrada("Digite algo:")
entrada("Digite outra coisa:")

#####################

def somar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

######
n1 = entrada("Digite um número:")
n2 = entrada("Digite outro número: ")

print(f"O resultado é: {somar(n1, n2)}")

