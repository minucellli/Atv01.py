#Dado um salário inicial e um aumento percentual que dobra a cada ano, calcule o salário atual após vários anos.
salario_inicial = float(input("Digite o salário inicial: "))
aumento_percentual = float(input("Digite o aumento percentual inicial (em %): "))
quantidade_anos = int(input("Digite o número de anos: "))

aumento_percentual /= 100
salario_atual = salario_inicial
for ano in range(1, quantidade_anos + 1):
    salario_atual += salario_atual * aumento_percentual
    aumento_percentual *= 2
print(f"O salário após {quantidade_anos} ano(s) é: R$ {salario_atual:}")
