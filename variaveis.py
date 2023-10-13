numero1 = int(input("Digite o número 1: "))

numero2 = int(input("Digite o número 2: "))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * 2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2
resto_da_divisao = numero1 % numero2
print("A soma dos números é:", soma )
print("A subtração é:" , subtracao)
print ("A mutiplicação é:", multiplicacao)
print ("A divisão é:" , divisao)
print ("A divisão inteira é:" , divisao_inteira)
print ("O resto da divisão é:" , resto_da_divisao)
#Maneira de printar o resultado colocando o .format
print("A soma de {} com {} é {}" .format(numero1, numero2, soma))
#Outra maneira colocando o f
print(f"A subtração de {numero1} com {numero2} é {subtracao}")
print(f"A multiplicacao de {numero1} com {numero2} é {multiplicacao}")
print(f"A divisão de {numero1} com {numero2} é {divisao}")
print(f"A divisão inteira de {numero1} com {numero2} é {divisao_inteira}")
print(f"O resto da divisão de {numero1} com {numero2} é {resto_da_divisao}")





