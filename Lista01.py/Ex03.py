#Peça ao usuário o valor total das mercadorias compradas. Se for menor que R$500, não há imposto. Caso contrário, aplique uma taxa de 50% sobre o valor que ultrapassar os R$500.
valor_compras = float(input("Digite o valor total das mercadorias compradas: "))
if valor <= 500: 
    print("Não há imposto.")
else:
    impostos = (valor - 500) * 0.5
    print(f"O valor do imposto a ser pago na compra é de R$ {impostos:}")
