numeros = list()
num = 0
while True:
    num = int(input("Digite um valor! "))
    if numeros.count(num) == 0:
        numeros.append(num)
    else:
        print("Valor duplicado! Não vou adicionar.")
    continuar = input("Deseja continuar? S/N ")
    if continuar == "N":
        break

#for n in numeros:
#    for i in range(0, len(numeros)):
#       for j in range(0, len(numeros)):
#            if n > numeros[i]:
numeros.sort()            
print(numeros)