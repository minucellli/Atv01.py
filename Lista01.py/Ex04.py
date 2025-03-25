#Um cliente alugou um carro e rodou alguns quilômetros por um certo número de dias. O custo diário é de R$90. Se ele rodou mais de 100 km, há uma taxa extra de R$12 por km adicional. Calcule o valor total a ser pago.
dias = int(input("Digite o número de dias que o carro foi alugado: "))
quilometros = float(input("Digite a quantidade de quilômetros rodados: "))
custo_diario = dias * 90
if quilometros > 100:
    custo_quilometro = (quilometros - 100) * 12
else:
    custo_km = 0
total = custo_diario + custo_quilometro
print(f"O valor total a ser pago é de R$ {total:}")
