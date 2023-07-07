pessoas = []
pessoa = []
maiorPeso = menorPeso = 0

print("-Programa Maior e Menor Peso-")

while True:
    cont = ""
    pessoa = [str(input("Informe o nome: ")), float(input("Informe o peso: "))]
    pessoas.append(pessoa[:])
    while cont == "":
        cont = str(input("Deseja continuar?[S/N] "))
        if cont == "S":
            continue
        elif cont == "N":
            break
        else:
            print("Resposta inválida. Tente novamente.")
            cont = ""
    if cont == "N":
        break
print(f"{len(pessoas)} foram cadastradas.")
maiorPeso = menorPeso = pessoas[0][1]
for p in pessoas:
    if p[1] >= maiorPeso:
        maiorPeso = p[1]
    if p[1] <= menorPeso:
        menorPeso = p[1]
for pos, p in enumerate(pessoas):
    if p[1] == maiorPeso:
        print(f"{p[0]} possui o maior peso, pesando {p[1]}. Ele está na posição {pos} da lista.")
for pos, p in enumerate(pessoas):
    if p[1] == menorPeso:
        print(f"{p[0]} possui o maior peso, pesando {p[1]}. Ele está na posição {pos} da lista.")