#from lampada import Lampada
#lampada1 = Lampada("amarela", 20, 220)
#lampada1 = liga()

#print("Lampada: {lampada1}") 
from conta import ContaPoupanca, ContaCorrente

conta_pedro =  Conta(123, 147, "Pedro" )

conta_jose =  Conta(456, 147, "José" )

print(f"O saldo de {conta_pedro.titular} é {conta_pedro.saldo}")

conta_pedro.depositar(1000)
conta_jose.depositar(1000)
print(f"O saldo de {conta_pedro.titular} é {conta_pedro.saldo}")
print(f"O saldo de {conta_jose.titular} é {conta_jose.saldo}")

conta_pedro.transferir(500, conta_jose)

conta_daniele = (200, 100, "Daniele")

conta_daniele.depositar(1000)

