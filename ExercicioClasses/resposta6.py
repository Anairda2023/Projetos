class TV:
    def __init__(self):
        self.canal = 4  # Canal inicial
        self.volume = 10  # Nível de volume inicial

    def alterar_canal(self, novo_canal):
        if 4 <= novo_canal <= 75:
            self.canal = novo_canal
            print(f"Canal alterado para {self.canal}")
        else:
            print("Canal inválido. O canal deve estar entre 4 e 75.")

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")
        else:
            print("Volume máximo atingido.")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")
        else:
            print("Volume mínimo atingido.")

    def imprimir_informacoes(self):
        print(f"Canal: {self.canal}")
        print(f"Volume: {self.volume}")

# Função para exibir o menu
def mostrar_menu():
    print("\nMenu:")
    print("1. Alterar Canal")
    print("2. Aumentar Volume")
    print("3. Diminuir Volume")
    print("4. Sair")

# Programa principal
tv = TV()

while True:
    tv.imprimir_informacoes()
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        novo_canal = int(input("Informe o número do novo canal: "))
        tv.alterar_canal(novo_canal)
    elif opcao == '2':
        tv.aumentar_volume()
    elif opcao == '3':
        tv.diminuir_volume()
    elif opcao == '4':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
