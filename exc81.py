lista = []
while True:
    lista.append(int(input("Digite um valor: ")))
    cont = input("Deseja continuar?(S/N) ")
    if cont == "S":
        continue
    elif cont == "N":
        break
lista.sort(reverse=True)
print(F"Você digitou {len(lista)} elementos.")
print(f"Os valores em ordem decrescente são: {lista}")
if lista.count(5) >= 1:
    print("O valor 5 faz parte da sua lista!")