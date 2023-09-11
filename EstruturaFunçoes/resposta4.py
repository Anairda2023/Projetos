
def verifica_argumento(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'        
    
num = float(input("Digite um número: "))

resultado = verifica_argumento(num)
print("Resultado:", resultado)   
    