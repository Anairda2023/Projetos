#Crie uma função que retorne o valor do  imposto de previdência de um dado salário
salario = float(input("Digite seu salário: "))
ip1 = [1]
if salario <= 1320:
    def ip1(salario):
        return salario * 0.075
    print("O imposto previdenciário é:")
break
elif 1301.01 <= salario <= 2571.29:
    def ip2(salario):
        return salario * 0.09
elif 2571.3 < salario < 3856.94:
    def ip3(salario):
        return salario * 0.012
else:
    def ip(salario):
        return salario * 0.014
soma = ip1 + ip2 + ip3
def ip(salario):
    return soma

print(ip)

#salario = float(input("Digite seu salário: "))

#def inss(salario):
#    ip = 0
#    if salario <= 1320:
#        ip = salario * 0.075
#        return(ip)
#    elif salario <= 2571.29:
#        ip1 = (salario - 1320.01) * 0.009 + ip 
#    elif salario <= 3856.94:
#        ip2 = (salario - 2571.3) * 0.012 + ip1
#    elif salario <= 7507.79:
#        ip3 = (salario - 3856.95) * 0.014 + ip2
#    return(ip3)

