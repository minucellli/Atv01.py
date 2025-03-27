#Peça três números ao usuário e informe qual é o maior e qual é o menor.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

maior = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
