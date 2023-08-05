contador = 1
resposta_nao_for_sim = True
while resposta_nao_for_sim:
    resposta = input(f"Tentativa {contador}\nVocê gosta de mim?\n")
    resposta_nao_for_sim = resposta != "sim"
    if resposta_nao_for_sim:
        print("Que pena, repita novamente")
    else:
        print("Parabéns, você é um ótimo amigo")
    #contador = contador + 1
    contador += 1
