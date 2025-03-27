#Solicite um número inteiro maior que 1 e verifique se ele é primo.
numero = int(input("Digite um número maior que 1: "))
if numero <= 1:
    print("Por favor, insira um número maior que 1.")
else:
    numero_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            numero_primo = False
            break

    if numero_primo:
        print(f"O número {numero} é primo!")
    else:
        print(f"O número {numero} não é primo.")
