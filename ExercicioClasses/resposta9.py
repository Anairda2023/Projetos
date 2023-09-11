class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Ponto ({self.x}, {self.y})")


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        x_centro = self.ponto_inicial.x + self.largura / 2
        y_centro = self.ponto_inicial.y + self.altura / 2
        return Ponto(x_centro, y_centro)

    def imprimir_centro(self):
        centro = self.encontrar_centro()
        print(f"Centro do Retângulo: ({centro.x}, {centro.y})")


# Função para criar um novo retângulo
def criar_retangulo():
    x = float(input("Digite a coordenada x do ponto inicial do retângulo: "))
    y = float(input("Digite a coordenada y do ponto inicial do retângulo: "))
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    ponto_inicial = Ponto(x, y)
    return Retangulo(ponto_inicial, largura, altura)


# Menu interativo
while True:
    print("\nMenu:")
    print("1. Criar um novo retângulo")
    print("2. Encontrar o centro de um retângulo")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        retangulo = criar_retangulo()
        print("Retângulo criado:")
        retangulo.ponto_inicial.imprimir()
    elif escolha == '2':
        if 'retangulo' in locals():
            retangulo.imprimir_centro()
        else:
            print("Crie um retângulo primeiro.")
    elif escolha == '3':
        break
    else:
        print("Opção inválida. Tente novamente.")
