numeros = (int(input()), int(input()), int(input()), int(input()))
print(numeros)
#Quantas vezes apareceu o valor 9:
if numeros.count(9) == 1:
    print(f"O valor 9 apareceu {numeros.count(9)} vez.")
print(f"O valor 9 apareceu {numeros.count(9)} vezez.")
#Em que posição foi digitado o primeiro valor 3:
if numeros.count(3) == 0:
    print("A tupla não possui o valor 3.")
else:
    print(f"O primeiro valor 3 foi digitado na posição: {numeros.index(3) + 1}.")
#Os números pares foram:
print("Os números pares digitados foram:", end=' ')
for num in numeros:
    if num % 2 == 0:
        print(f"{num} ", end='')