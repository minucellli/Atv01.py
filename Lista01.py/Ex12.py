#Peça ao usuário a quantidade de turmas e a quantidade total de alunos. Informe a média de alunos por turma, mas avise se alguma turma tiver mais de 40 alunos
quantidade_turmas = int(input("Digite quantas turmas tem: "))
total_alunos = 0

for turma in range(1, quantidade_turmas + 1):
    alunos = int(input(f"Digite a quantidade de alunos da turma {turma}: "))
    if alunos > 40:
        print("Uma turma não pode ter mais de 40 alunos!")
    total_alunos += alunos

media = total_alunos / quantidade_turmas
print(f"A média de alunos por turma é: {media:}")
