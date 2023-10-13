
from conta import ContaCorrente, ContaPoupanca

#Criando uma instância de lâmpada (amarela, 20, 200) - como eu construo meu objeto = Lampada()

#lampada1 = Lampada("amarela", 20, 220)

#lampada1.ligar()

#print(lampada1.potencia)

#lampada1.potencia = -2

#print(lampada1.potencia)

conta_pedro = ContaCorrente(123, 147, "Pedro")

conta_jose = ContaCorrente(456, 147, "José")

conta_jose.depositar(1000)

print(conta_jose)

conta_daniele = ContaPoupanca(963, 854, "Daniele")

conta_daniele.depositar(1000)

print(conta_daniele)

conta_jose.sacar(1500)


print(conta_jose)



