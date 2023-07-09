numeros = list()
while True:
    numeros.append(int(input("Digite um valor: ")))
    cont = str(input("Deseja continuar?(S/N) "))
    if cont != "S" or cont != "N":
        while cont != "S" or cont != "N":
            cont = input("Deseja continuar?(S/N) ")
            if cont == "S" or cont == "N":
                break
    if cont == "S":
        continue
    elif cont == "N":
        break