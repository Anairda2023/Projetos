def bem_vindo():
    print("Bem vindo!")

def entrada(texto):
    return int(input(texto))

def somar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def inss(salario):
    faixa1 = salario <= 1320
    faixa2 = salario > 1320 and salario <= 2571.29
    faixa3 = salario > 2571.29 and salario <= 3856.94
    faixa4 = salario > 3856.94 and salario <= 7507.49

    if faixa1:
        return salario * 0.075
    elif faixa2:
        return (salario - 1320.01) * 0.09 + 99
    elif faixa3:
        return (salario - 2571.30) * 0.12 + 211.62
    elif faixa4:
        return (salario - 3856.95) * 0.14 + 365.89
    return 876.97
