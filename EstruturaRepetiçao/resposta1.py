while True:
    x = float(input("Insira uma nota de zero à dez: "))
    if 0 <=  x <= 10:
        break
    else:
        print("O Valor da nota é inválido. A nota deve estar entre zero e dez.")
print(f"O valor da nota válido é: {x}")

   
