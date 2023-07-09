lanche = "Pão", "Croissant", "Coxinha"

for pos, comida in enumerate(lanche):
    if pos == 0:
        if comida[-1] == "a":
            print(f"Primeiro eu comi uma {comida}, ")
        else:
            print(f"Primeiro eu comi um {comida}, ")
    if pos == 1:
        if comida[-1] == "a":
            print(f"depois eu comi uma {comida} e, ")
        else:
            print(f"depois eu comi um {comida} e, ")
    if pos == 2:
        if comida[-1] == "a":
            print(f"por fim, eu comi uma {comida}")
        else:
            print(f"por fim, eu comi um {comida}")
