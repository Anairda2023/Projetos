from lampada import Lampada
from conta import Conta

#Criando uma instância de lâmpada (amarela, 20, 200) - como eu construo meu objeto = Lampada()

#lampada1 = Lampada("amarela", 20, 220)

#lampada1.ligar()

#print(lampada1.potencia)

#lampada1.potencia = -2

#print(lampada1.potencia)

conta_pedro = Conta(123, 147, "Pedro")


conta_pedro.depositar(20)

print(f"Saldo de {conta_pedro.titular} é: {conta_pedro.saldo}")

conta_jose = Conta(456, 147, "José")

conta_jose.depositar(500)

print(f"Saldo de {conta_jose.titular} é {conta_jose.saldo}")


