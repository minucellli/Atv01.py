#Solicite um valor em segundos e converta para dias, horas e minutos. 
segundos = int(input("Digite um valor em segundos: "))
dias = segundos // 86400
print(f"{segundos} segundos equivale a: {dias} dias.")
horas = segundos // 3600
print(f"{segundos} segundos equivale a: {horas} horas.")
minutos = segundos // 60
print(f"{segundos} segundos equivale a: {minutos} minutos.") 

# o dia equivale a = 86400 segundos
# a hora equivale a = 3600 segundos
# o minuto equivale a = 60 segundos
