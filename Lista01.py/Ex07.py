#Solicite um número ímpar ao usuário e calcule a diferença entre o quadrado do número anterior e do próximo número ímpar.
numero = int(input("Digite um número ímpar: "))
if numero % 2 == 0:
    print(f"O número {numero} não é ímpar.")
else:
    numero_ante = numero - 2
    numero_pos = numero + 2
    quadrado_ante = numero_ante ** 2
    quadrado_post = numero_pos ** 2
    diferenca = quadrado_post - quadrado_ante
    print(f"A diferença entre o quadrado do número anterior e do próximo número ímpar é: {diferenca}")
