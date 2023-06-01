alunos = []
tamTurma = int(input("Digite o tamanho da turma.\n"))
for i in range(1, tamTurma + 1):
    ele = input(f"Digite o nome do aluno {i}\n")
    alunos.append(ele)
materias = []
qtdMateria = int(input("Digite a quantidade de matérias.\n"))
for i in range(1, qtdMateria + 1):
    ele = input(f"Digite o nome da matéria {i}\n")
    materias.append(ele)
notas = []
contNotas = 0
for i in alunos:
    j = 1
    ele = []
    while j <= qtdMateria:
        ele += [int(input(f"Digite a nota de {i}\n"))]
        j += 1
    notas.append(ele)
print(alunos, f"\n{materias}", f"\n{notas}")
k = 0
j = 0
media = 0
for i in alunos:
    for f in materias:
        if k==0:
            print(f"{i} tirou {notas[k][j]} em {materias[j]}.")
            media += notas[k][j]
            j+=1
            continue
        if k==1:
            print(f"{i} tirou {notas[k][j]} em {materias[j]}.")
            media += notas[k][j]
            j+=1
            continue
        if k==2:
            print(f"{i} tirou {notas[k][j]} em {materias[j]}.")
            media += notas[k][j]
            j+=1
            continue
    print("-"*25)
    print(f"A média de {i} é {media/qtdMateria:.1f}")
    print("-"*25)
    j=0
    k+=1
    media = 0