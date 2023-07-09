numeros = list() 
for n in range(1,6): 
    if n == 1: 
        numeros.append(int(input("Digite um valor: "))) 
        print("Adicionado ao final da lista...") 
    if n == 2: 
        v2 = int(input("Digite outro valor: ")) 
        if v2 < numeros[0]: 
            numeros.insert(0, v2) 
            print("Adicionado na posição 0 da lista...") 
        else: 
            numeros.append(v2) 
            print("Adicionado ao final da lista...") 
    if n == 3: 
        v3 = int(input("Digite outro valor: ")) 
        if v3 < numeros[0]: 
            numeros.insert(0, v3) 
            print("Adicionado na posição 0 da lista...") 
        elif v3 > numeros[1]: 
            numeros.append(v3) 
            print("Adicionado ao final da lista...") 
        else: 
            numeros.insert(1, v3) 
            print("Adicionado na posição 1 da lista...") 
    if n == 4: 
        v4 = int(input("Digite outro valor: ")) 
        if v4 < numeros[0]: 
            numeros.insert(0, v4) 
            print("Adicionado na posição 0 da lista...") 
        elif v4 > numeros[0] and v4 < numeros[1]: 
            numeros.insert(1, v4) 
            print("Adicionado na posição 1 da lista...") 
        elif v4 > numeros[1] and v4 < numeros[2]:
            numeros.insert(2, v4) 
            print("Adicionado na posição 2 da lista...") 
        else: 
            numeros.append(v4) 
            print("Adicionado ao final da lista...") 
    if n == 5: 
        v5 = int(input("Digite outro valor: ")) 
        if v5 < numeros[0]: 
            numeros.insert(0, v5) 
            print("Adicionado na posição 0 da lista...") 
        elif v5 > numeros[0] and v5 < numeros[1]: 
            numeros.insert(1, v5) 
            print("Adicionado na posição 1 da lista...") 
        elif v5 > numeros[1] and v5 < numeros[2]: 
            numeros.insert(2, v5) 
            print("Adicionado na posição 2 da lista...") 
        elif v5 > numeros[2] and v5 < numeros[3]: 
            numeros.insert(3, v5) 
            print("Adicionado na posição 3 da lista...") 
        else: 
            numeros.append(v5) 
            print("Adicionado ao final da lista...")
print(numeros)