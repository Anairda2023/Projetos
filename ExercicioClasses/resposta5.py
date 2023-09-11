class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def saque(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser maior que zero.")

    def imprimirInformacoes(self):
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Nome do Correntista: {self.nome_correntista}")
        print(f"Saldo: R${self.saldo:.2f}")


conta1 = ContaCorrente("12345-6", "Drika", 1000.0)
conta1.imprimirInformacoes()

conta1.deposito(500.0)
conta1.saque(200.0)

conta1.alterarNome("Adri")
conta1.imprimirInformacoes()
