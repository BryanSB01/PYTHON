numeros = list()
maior = menor = 0
numeros.append(int(input(f"Digite um número para a posição 0: ")))
maior = menor = numeros[0]
for i in range(1,5):
    numeros.append(int(input(f"Digite um número para a posição {i}: ")))
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]
print(f"Sua lista é: {numeros}")
print(f"O maior valor foi {maior}. Apareceu nas posições: ", end='')
for pos, n in enumerate(numeros):
    if n == maior:
        print(f"{pos}", end=' ')
print(f"\nO menor valor foi {menor}. Apareceu nas posições: ", end='')
for pos, n in enumerate(numeros):
    if n == menor:
        print(f"{pos}", end=' ')