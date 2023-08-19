produto1 = input("Informe o nome do produto 1: \n")
preco1 = float(input(f"Informe o preço do {produto1}:"))

produto2 = input("Informe o nome do produto 2: \n")
preco2 = float(input(f"Informe o preço do {produto2}:"))

produto3 = input("Informe o nome do produto 3: \n")
preco3 = float(input(f"Informe o preço do {produto3}:"))

menor = preco1
melhor_produto = produto1
if (preco2 < menor):
    menor = preco2
    melhor_produto = produto2

if (preco3 < menor):
    menor = preco3
    melhor_produto = produto3
print(f"o melhor produto é {melhor_produto} com preço R$ {menor}")
