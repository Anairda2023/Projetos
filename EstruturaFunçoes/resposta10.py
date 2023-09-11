import random

def jogar_craps():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    print(f"Você lançou os dados e obteve {dado1} e {dado2} (total: {soma})")

    if soma == 7 or soma == 11:
        print("Natural! Você ganhou!")
    elif soma == 2 or soma == 3 or soma == 12:
        print("Craps! Você perdeu.")
    else:
        ponto = soma
        print(f"Ponto é {ponto}. Continue jogando.")

        while True:
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            nova_soma = dado1 + dado2
            print(f"Você lançou os dados e obteve {dado1} e {dado2} (total: {nova_soma})")

            if nova_soma == ponto:
                print("Você acertou o ponto! Você ganhou!")
                break
            elif nova_soma == 7:
                print("Você tirou 7! Você perdeu.")
                break

# Início do jogo
print("Bem-vindo ao jogo de Craps!")
while True:
    jogar = input("Deseja jogar? (S/N): ")
    if jogar.lower() == 's':
        jogar_craps()
    else:
        print("Obrigado por jogar!")
        break
