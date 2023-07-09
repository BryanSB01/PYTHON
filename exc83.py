exp = str(input("Digite uma expressão matemática. "))
abr = exp.count("(")
fcd = exp.count(")")
if abr == fcd:
    print("Sua expressão está correta!")
elif abr != fcd:
    print("Sua expressão está incorreta!")