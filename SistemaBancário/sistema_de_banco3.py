import re
import datetime

menu = """
[c] Criar Usuário
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
data_hora = str(datetime.datetime.now()).split( )
data = data_hora[0].split("-")
dia = data[2]
mes = data[1]
ano = data[0]

#Classe Usuários:
class Usuario():
    def __init__(self, nome, data_nascimento):
        nome.self = nome
        data_nascimento.self = data_nascimento

#Função para criar usuário:
def criar_usuario():
    nome = input("Informe o nome de usuário: ")
    padrao_data_nascimento = r'([0-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/(19[2-9][0-9]|20[0-1][0-9]|202[0-4])'
    data_nascimento = input("Informe a data de nascimento: ")
    if data_nascimento[0:2] > dia and data_nascimento[3:5] == mes and data_nascimento[6:11] == ano:
        print("Esse dia ainda não chegou")
    elif data_nascimento[3:5] > mes and data_nascimento[6:11] == ano:
        print("Esse mês ainda não chegou")
    try:
        while re.search(padrao_data_nascimento, data_nascimento) == None:
            raise ValueError("Data inválida")
    except ValueError as e:
        print(30*"#")
        print("Erro:", e, "\nTente novamente!")
        print(30*"#")
        data_nascimento = input("Informe a data de nascimento: ")
    cpf = input("Informe o CPF: ")
    endereco = input("Informe o endereço: ")
    
    

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
    
    #Criar Usuário
    if opcao == "c":
        criar_usuario()
    
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
