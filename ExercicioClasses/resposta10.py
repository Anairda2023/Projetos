class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        if valor > 0:
            litros_abastecidos = valor / self.valor_litro
            if litros_abastecidos <= self.quantidade_combustivel:
                self.quantidade_combustivel -= litros_abastecidos
                print(f"Abastecimento de R${valor:.2f} realizado. Foram adicionados {litros_abastecidos:.2f} litros de {self.tipo_combustivel}.")
            else:
                print("Não há combustível suficiente na bomba.")
        else:
            print("O valor do abastecimento deve ser maior que zero.")

    def abastecer_por_litro(self, litros):
        if litros > 0:
            valor_pagar = litros * self.valor_litro
            if litros <= self.quantidade_combustivel:
                self.quantidade_combustivel -= litros
                print(f"Abastecimento de {litros:.2f} litros de {self.tipo_combustivel} realizado. Valor a pagar: R${valor_pagar:.2f}")
            else:
                print("Não há combustível suficiente na bomba.")
        else:
            print("A quantidade de litros deve ser maior que zero.")

    def alterar_valor(self, novo_valor):
        if novo_valor > 0:
            self.valor_litro = novo_valor
            print(f"Valor do litro de {self.tipo_combustivel} alterado para R${novo_valor:.2f}")
        else:
            print("O novo valor deve ser maior que zero.")

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel
        print(f"Tipo de combustível alterado para {novo_combustivel}")

    def alterar_quantidade_combustivel(self, nova_quantidade):
        if nova_quantidade >= 0:
            self.quantidade_combustivel = nova_quantidade
            print(f"Quantidade de combustível atualizada para {nova_quantidade:.2f} litros.")
        else:
            print("A quantidade de combustível deve ser maior ou igual a zero.")

    def mostrar_status(self):
        print(f"Tipo de Combustível: {self.tipo_combustivel}")
        print(f"Valor do Litro: R${self.valor_litro:.2f}")
        print(f"Quantidade de Combustível: {self.quantidade_combustivel:.2f} litros")

# Exemplo de uso da classe
bomba = BombaCombustivel("Gasolina", 4.50, 1000.0)

bomba.mostrar_status()
bomba.abastecer_por_valor(50)
bomba.abastecer_por_litro(10)
bomba.alterar_valor(4.60)
bomba.alterar_combustivel("Etanol")
bomba.alterar_quantidade_combustivel(1500)
bomba.mostrar_status()
