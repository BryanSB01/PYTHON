menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
contadora = 0
saldo = 0
limite = 500
texto_extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


#Função para depósito:
def deposito(valor_deposito, /):
    global saldo 
    global texto_extrato
    titulo = " DEPÓSITO ".center(40, "#")
    print(f"{titulo}")
    while valor_deposito <= 0:
        print("\nO valor para depósito não pode ser menor ou igual à zero!")
        valor_deposito = int(input("\nInforme o valor que deseja depositar: "))
    saldo += valor_deposito
    texto_extrato += f"Depósito de R${valor_deposito:.2f}\n"
    print(f"\nVocê depositou R${valor_deposito:.2f}", end=" ")
    print("\U0001F389")
    print(f"\n{40 * '#'}")

#Função para saque:
def saque(*, valor_saque=None):
  global saldo 
  global texto_extrato
  global contadora
  titulo = " SAQUE ".center(40, "#")
  print(f"{titulo}")
  if saldo > 0:    
      if contadora < 3:
          while valor_saque > limite:
              print("\n\u001b[31mX\u001b[0m ", end="")
              print("O limite de saque é de R$500,00!")
              valor_saque = int(input("\nInforme o valor que deseja sacar: "))
          while valor_saque <= 0:
              print("O valor para saque não pode ser menor ou igual à zero!")
              valor_saque = int(input("\nInforme o valor que deseja sacar: "))
          while valor_saque > saldo:
              print("Saldo insuficiente. Tente outro valor!")
              valor_saque = int(input("Informe o valor que deseja sacar: "))
          saldo -= valor_saque
          texto_extrato += f"Saque de R${valor_saque:.2f}\n"
          contadora += 1
          print(f"\nVocê sacou R${valor_saque:.2f}", end="")
          print("\U0001F4B2")
      else:
          print("\nLimite Diário de Saques Bancários Atingido")
  else:
      print("\nVocê não possui dinheiro para sacar!")
  print(f"\n{40 * '#'}")

#Função para extrato:
def extrato():
  global saldo
  global texto_extrato
  titulo = " EXTRATO ".center(40, "#")
  print(f"{titulo}")
  print(f"\nExtrato:\n\n{texto_extrato}\nSeu saldo é: R${saldo:.2f}")
  print(f"\n{40 * '#'}")


#Função para sair:
def sair():
  print("""Muito obrigado por utilizar nosso sistema!
Até a próxima! \U0001F60A
        """)

print(
f"""
{" Sistema Bancário ".center(46,"#")}

- Seja bem vindo ao Banco dos Desenvolvedores.

Escolha uma das operações a seguir:""")
while True:
    opcao = input(menu)
    print("")
    
    #Depósito
    if opcao == "d":
        valor = int(input("Informe o valor que deseja depositar: "))
        print("\n")
        deposito(valor)
    #Saque
    elif opcao == "s":
        valor = int(input("Informe o valor que deseja sacar: "))
        print("\n")
        saque(valor_saque=valor)
    #Extrato    
    elif opcao == "e":
        extrato()
    #Sair
    elif opcao == "q":
        sair()
        break
