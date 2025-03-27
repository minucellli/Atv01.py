#Crie um programa que gere e exiba os 100 primeiros números primos.
def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primos = []
n = 2

while len(primos) < 100:
    if primo(n):
        primos.append(n)
    n += 1

print("Os 100 primeiros números primos são: ")
print(primos)
