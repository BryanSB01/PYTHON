menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
contadora = 0
contadora_exec = 0
saldo = 0
#LIMITE_VALOR = 500
extrato = ""
#LIMITE_SAQUES = 3

def deposito():
    global saldo
    global extrato
    titulo = " DEPÓSITO ".center(40, "#")
    print(f"{titulo}")
    valor_deposito = float(input("""\nInforme o valor que deseja depositar: """))
    while valor_deposito <= 0:
        print("\nO valor para depósito não pode ser menor ou igual à zero!")
        valor_deposito = float(input("\nInforme o valor que deseja depositar: "))
    saldo += valor_deposito
    extrato += f"Depósito de R${valor_deposito:.2f}\n"
    print(f"\nVocê depositou R${valor_deposito:.2f}", end=" ")
    print("\U0001F389")
    print(f"\n{40 * '#'}")

def saque(*, saldo, extrato, contadora, LIMITE_VALOR, LIMITE_SAQUES):

    titulo = " SAQUE ".center(40, "#")
    print(f"{titulo}")

    if saldo > 0:    
        if contadora < LIMITE_SAQUES:
            valor_saque = float(input("\nInforme o valor que deseja sacar: "))
            while valor_saque <= 0:
                print("O valor para saque não pode ser menor ou igual à zero!")
                valor_saque = float(input("\nInforme o valor que deseja sacar: "))
            while valor_saque > LIMITE_VALOR:
                print("\nO valor para saque não pode ser maior que 500!")
                valor_saque = float(input("\nInforme o valor que deseja sacar: "))
            while valor_saque > saldo:
                print("Saldo insuficiente. Tente outro valor!")
                valor_saque = float(input("Informe o valor que deseja sacar: "))
            saldo -= valor_saque
            extrato += f"Saque de R${valor_saque:.2f}\n"    
            contadora += 1
            print(f"\nVocê sacou R${valor_saque:.2f}.", end="")
            print("\U0001F4B2")
        else:
            print("\nLimite Diário de Saques Bancários Atingido")
    else:
        print("\nVocê não possui dinheiro para sacar!")
    print(f"\n{40 * '#'}")

def mostra_extrato(extrato, saldo):
    titulo = " EXTRATO ".center(40, "#")
    print(f"{titulo}")
    print(f"\nExtrato:\n\n{extrato}\nSeu saldo é: R${saldo:.2f}")
    print(f"\n{40 * '#'}")

def sair():
    print(f"{40 * '#'}\n")
    print("""Muito obrigado por utilizar nosso sistema!
Até a próxima! \U0001F60A
    """)
    print(f"{40 * '#'}")

print(
f"""
{" Sistema Bancário ".center(46,"#")}

- Seja bem vindo ao Banco dos Desenvolvedores.

Escolha uma das operações a seguir:""")

while True:

    if contadora_exec >= 1:
        print("\nEscolha uma das operações a seguir:")

    opcao = input(menu)
    print("")
    
    if opcao == "d":
        deposito()
        contadora_exec += 1
        
    elif opcao == "s":
        saque(saldo=saldo, extrato="", contadora=0, LIMITE_SAQUES=3, LIMITE_VALOR=500)
        contadora_exec += 1

    elif opcao == "e":
        mostra_extrato(extrato=extrato, saldo=saldo)
        contadora_exec += 1

    elif opcao == "q":
        sair()
        break
