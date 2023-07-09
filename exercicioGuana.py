try:
    n1 = int(input("Digite um número inteiro: " ))
except Exception as erro:
    print("Tente novamente.", erro.__class__, erro.__context__)