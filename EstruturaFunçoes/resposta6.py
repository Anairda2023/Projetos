def converter_para_12_horas(horas24, minutos):
    periodo = 'A'
    if horas24 >= 12:
        periodo = 'P'
    if horas24 == 0 or horas24 == 12:
        horas12 = 12
    else:
        horas12 = horas24 % 12
    return horas12, periodo, minutos

def imprimir_hora(horas12, periodo, minutos):
    print(f"{horas12}:{minutos:02d} {periodo}.M.")

# Loop principal
while True:
    try:
        horas24 = int(input("Digite a hora (0-23): "))
        minutos = int(input("Digite os minutos (0-59): "))
        
        if 0 <= horas24 <= 23 and 0 <= minutos <= 59:
            horas12, periodo, minutos = converter_para_12_horas(horas24, minutos)
            imprimir_hora(horas12, periodo, minutos)
        else:
            print("Valores inválidos. Tente novamente.")
        
        repetir = input("Deseja converter outra hora? (S/N): ")
        if repetir.lower() != 's':
            break
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números inteiros.")
