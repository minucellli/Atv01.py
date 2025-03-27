#Crie um sistema de login que não permite que o nome de usuário e a senha sejam iguais
nome_user = input("Digite seu nome de usuário: ")
senha = input("Digite a sua senha: ")
if nome_user == senha:
    print("Erro: O nome de usuário e a senha não podem ser iguais. Por favor, tente novamente.")
else:
    print("Login bem-sucedido!")
