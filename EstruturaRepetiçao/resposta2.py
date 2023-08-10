nome = input("Insira o nome do usuário: ")
while True:
    senha = input("Insira a senha: ")
    if nome == senha:
        print("O nome da senha não pode ser igual ao nome do usuário. Digite a senha novamente")
    else:    
        break
print("Você inseriu corretamente o Usuáro e a senha")        