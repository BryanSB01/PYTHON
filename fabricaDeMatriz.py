print("-"*10, "Fábrica de Matriz", "-"*10)
#Declarando as variáveis:
matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPares = 0
somaTerCol = 0
maiorValorSegLin = 0
#Formando a matriz com as entradas do usuário:
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para a linha {l} coluna {c}:"))
#Mostrando a matriz formada:
for l in range(0, 3):
    print("[", end="")
    for c in range(0, 3):
        print(f" {matriz[l][c]} ", end="")
    print("]")
#Mostrando a soma de todos os valores pares digitados:
for n in range(0, 3):
    for i in range(0, 3):
        if matriz[n][i] % 2 == 0:
            somaPares += matriz[n][i]
print(f"A soma de todos os valores pares digitados é: {somaPares}")
#Mostrando a soma de todos os valores da terceira coluna:
for n in range(0, 3):
    for i in range(0, 3):
        if i == 2:
            somaTerCol += matriz[n][i] 
print(f"A soma de todos os valores da terceira coluna é: {somaTerCol}")
#Mostrando o maior valor da segunda linha:
maiorValorSegLin = matriz[1][0]
for n in range(0, 3):
    for i in range(0, 3):
        if n == 1:
            if matriz[n][i] > maiorValorSegLin:
                maiorValorSegLin = matriz[n][i]
print(f"O maior valor da segunda linha é: {maiorValorSegLin}")