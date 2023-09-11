def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso == 0:
        valor_pago = valor_prestacao
    else:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * (dias_atraso * 0.001)
        valor_pago = valor_prestacao + multa + juros
    return valor_pago

# Inicializações
prestacoes_pagas = 0
total_valor_pago = 0

# Loop principal
while True:
    valor = float(input("Digite o valor da prestação (ou 0 para sair): "))
    
    if valor == 0:
        break
    
    dias_atraso = int(input("Digite o número de dias em atraso: "))
    
    valor_a_pagar = valorPagamento(valor, dias_atraso)
    print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
    
    prestacoes_pagas += 1
    total_valor_pago += valor_a_pagar

# Relatório do dia
print("\nRelatório do dia:")
print(f"Quantidade de prestações pagas: {prestacoes_pagas}")
print(f"Valor total pago no dia: R$ {total_valor_pago:.2f}")
