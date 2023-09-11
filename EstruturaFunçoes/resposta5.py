def somaImposto(taxaImposto, custo):
    custo_com_imposto = custo * (1 + taxaImposto / 100)
    return custo_com_imposto

# Solicita os valores ao usuário
taxa = float(input("Digite a taxa de imposto em porcentagem: "))
custo_item = float(input("Digite o custo do item antes do imposto: "))

custo_com_imposto = somaImposto(taxa, custo_item)
print("Custo com imposto: R$", custo_com_imposto)