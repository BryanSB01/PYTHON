import datetime
import random
import re


menu = """
[c] Criar Usuário
[d] Depositar
[s] Sacar
[e] Extrato
[m] Mostrar Dados do Usuário
[q] Sair

"""

# Classe Usuário:
class Usuario():

    contadora = 0
    limite = 500
    LIMITE_SAQUES = 3
    data_hora = str(datetime.datetime.now()).split()
    data = data_hora[0].split("-")
    dia = data[2]
    mes = data[1]
    ano = data[0]
    usuarios = []

    def __init__(self):
        titulo = " CADASTRO ".center(40, "#")
        print(f"{titulo}")
        padrao_nome = r'^[a-zA-Z]+( [a-zA-Z]+)?$'
        padrao_data_nascimento = r'([0-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/(19[2-9][0-9]|20[0-1][0-9]|202[0-4])'
        padrao_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
        self.nome = input("Informe o seu nome: ")
        while re.search(padrao_nome, self.nome) is None:
            try:
                while re.search(padrao_nome, self.nome) is None:
                    raise ValueError("Nome inválido")
            except ValueError as e:
                print(30 * "#")
                print("\033[1m\033[31mErro:", e, "\nTente novamente!\033[0m")
                print(30 * "#")
                self.nome = input("Informe o seu nome: ")
        self.data_nascimento = input("Informe sua data de nascimento: ")
        while self.data_nascimento[0:2] > Usuario.dia and self.data_nascimento[3:5] == Usuario.mes and self.data_nascimento[6:11] == Usuario.ano:
            print("\n", end = '')
            print(30 * "#")
            print("\033[1m\033[31mEsse dia ainda não chegou\033[0m")
            print(30 * "#", end = '')
            print("\n")
            self.data_nascimento = input("Informe sua data de nascimento: ")
        while self.data_nascimento[3:5] > Usuario.mes and self.data_nascimento[6:11] == Usuario.ano:
            print("Esse mês ainda não chegou")
            self.data_nascimento = input("Informe sua data de nascimento: ")
        while self.data_nascimento[6:11] > Usuario.ano:
            print("Esse ano ainda não chegou")
            self.data_nascimento = input("Informe sua data de nascimento: ")
        while re.search(padrao_data_nascimento, self.data_nascimento) is None:
            try:
                while re.search(padrao_data_nascimento, self.data_nascimento) is None:
                    raise ValueError("Data inválida")
            except ValueError as e:
                print(30 * "#")
                print("\033[1m\033[31mErro:", e, "\nTente novamente!\033[0m")
                print(30 * "#")
                self.data_nascimento = input("Informe a data de nascimento: ")
        self.cpf = input("Informe o CPF: ")
        while re.search(padrao_cpf, self.cpf) is None:
            try:
                while re.search(padrao_cpf, self.cpf) is None:
                    raise ValueError("CPF Inválido")
            except ValueError as e:
                print(30 * "#")
                print("\033[1m\033[31mErro:", e, "\nTente novamente!\033[0m")
                print(30 * "#")
                self.cpf = input("Informe o CPF: ")
        try:
            self.endereco = input("Informe o endereço: ")
        except UnicodeDecodeError as e:
            print(30 * "#")
            print("\033[1m\033[31mErro:", e, "\nTente novamente!\033[0m")
            print(30 * "#")
            self.endereco = input("Informe o endereço: ")
        self.numero_conta = None
        self.senha_conta = None
        self.sexo = input("Informe seu sexo (M-Masculino, F-Feminino): ").upper()
        self.saldo = 0
        self.texto_extrato = ""

    # Função para exibir os atributos do objeto:
    def __str__(self):
        return (f"Nome: {self.nome}\nData Nascimento: {self.data_nascimento}\nCPF: {self.cpf}\nEndereço: {self.endereco}\nID Conta: {self.numero_conta}\nSenha: {self.senha_conta}\nSaldo: {self.saldo}\nExtrato: {self.texto_extrato}")

    # Função para criar usuário:
    def cria_usuario(self):
        self.numero_conta = ''.join(random.choice('0123456789') for i in range(7))
        while self.numero_conta[0] == 0:
            self.numero_conta = self.numero_conta[1:]
            self.numero_conta += "0"
        while True:
            try:
                entrada = input("Crie uma senha para sua conta: ")
                if not entrada.strip():  # Verifica se a entrada está vazia ou contém apenas espaços em branco
                    raise ValueError("A entrada não pode ser vazia. Tente novamente!")
                self.senha_conta = entrada
                break  # Se a conversão for bem-sucedida, sair do loop
            except ValueError as e:
                print(30 * "#")
                print("\033[1m\033[31mErro:", e, "\nTente novamente!\033[0m")
                print(30 * "#")
        
        usuario = {"Nome": self.nome, "Data Nascimento": self.data_nascimento, "CPF": self.cpf, 
                   "Endereço": self.endereco, "ID Conta": self.numero_conta, "Senha": self.senha_conta, 
                   "Saldo": self.saldo, "Extrato": self.texto_extrato, "Instancia": self}
        Usuario.usuarios.append(usuario)
        if self.sexo == "M":
            print("\n")
            print(40 * "#")
            print(f"Parabéns {usuario['Nome']}, seja bem vindo ao Banco dos Desenvolvedores!\nO número da sua conta é: {usuario['ID Conta']}")
            print(40 * "#")
            print("\n")
        else:
            print("\n")
            print(40 * "#")
            print(f"Parabéns {usuario['Nome']}, seja bem vinda ao Banco dos Desenvolvedores!\nO número da sua conta é: {usuario['ID Conta']}")
            print(40 * "#")
            print("\n")

    # Função para depósito:
    def deposito(self, valor_deposito, /):
        titulo = " DEPÓSITO ".center(40, "#")
        print(f"{titulo}")
        while valor_deposito <= 0:
            print("\nO valor para depósito não pode ser menor ou igual à zero!")
            valor_deposito = int(input("\nInforme o valor que deseja depositar: "))
        self.saldo += valor_deposito
        self.texto_extrato += f"Depósito de R${valor_deposito:.2f}\n"
        print(f"\nVocê depositou R${valor_deposito:.2f}", end=" ")
        print("\U0001F389")
        print(f"\n{40 * '#'}")
        return self.saldo

    # Função para saque:
    def saque(self, *, valor_saque=None):
        titulo = " SAQUE ".center(40, "#")
        print(f"{titulo}")
        if self.saldo > 0:
            if usuario.contadora < Usuario.LIMITE_SAQUES:
                while valor_saque > Usuario.limite:
                    print("\n\u001b[31mX\u001b[0m ", end="")
                    print("O limite de saque é de R$500,00!")
                    valor_saque = int(input("\nInforme o valor que deseja sacar: "))
                while valor_saque <= 0:
                    print("O valor para saque não pode ser menor ou igual à zero!")
                    valor_saque = int(input("\nInforme o valor que deseja sacar: "))
                while valor_saque > self.saldo:
                    print("Saldo insuficiente. Tente outro valor!")
                    valor_saque = int(input("Informe o valor que deseja sacar: "))
                self.saldo -= valor_saque
                self.texto_extrato += f"Saque de R${valor_saque:.2f}\n"
                usuario.contadora += 1
                print(f"\nVocê sacou R${valor_saque:.2f}", end="")
                print("\U0001F4B2")
            else:
                print("\nLimite Diário de Saques Bancários Atingido")
        else:
            print("\nVocê não possui dinheiro para sacar!")
        print(f"\n{40 * '#'}")

    # Função para extrato:
    def extrato(self):
        titulo = " EXTRATO ".center(40, "#")
        print(f"{titulo}")
        print(f"\nExtrato:\n\n{self.texto_extrato}\nSeu saldo é: R${self.saldo:.2f}")
        print(f"\n{40 * '#'}")
        return f"\nExtrato:\n\n{self.texto_extrato}\nSeu saldo é: R${self.saldo:.2f}"

    # Função para sair:
    def sair(self):
        print("""Muito obrigado por utilizar nosso sistema!
Até a próxima! \U0001F60A
        """)

print(
f"""
{" Sistema Bancário ".center(46, "#")}

- Seja bem vindo ao Banco dos Desenvolvedores.

Escolha uma das operações a seguir:""")
while True:
    
    opcao = input(menu)
    print("")

    # Criar Usuário
    if opcao == "c":
        usuario = Usuario()
        usuario.cria_usuario()

    # Depósito
    elif opcao == "d":
        ID = input("Informe o ID da conta: ")
        senha = input("Informe a senha da conta: ")
        for i in range(len(Usuario.usuarios)):
            if ID == Usuario.usuarios[i]["ID Conta"] and senha == Usuario.usuarios[i]["Senha"]:
                valor = int(input("Informe o valor que deseja depositar: "))
                print("\n")
                Usuario.usuarios[i]["Instancia"].deposito(valor)

    # Saque
    elif opcao == "s":
        ID = input("Informe o ID da conta: ")
        senha = input("Informe a senha da conta: ")
        for i in range(len(Usuario.usuarios)):
            if ID == Usuario.usuarios[i]["ID Conta"] and senha == Usuario.usuarios[i]["Senha"]:
                valor = int(input("Informe o valor que deseja sacar: "))
                print("\n")
                Usuario.usuarios[i]["Instancia"].saque(valor_saque=valor)
            else:
                continue

    # Extrato    
    elif opcao == "e":
        ID = input("Informe o ID da conta: ")
        senha = input("Informe a senha da conta: ")
        for i in range(len(Usuario.usuarios)):
            if ID == Usuario.usuarios[i]["ID Conta"] and senha == Usuario.usuarios[i]["Senha"]:
                print("\n")
                Usuario.usuarios[i]["Instancia"].extrato()
            else:
                continue

    # Mostrar Dados do Usuário    
    elif opcao == "m":
        try:
            ID = input("Informe o ID da conta: ")
            senha = input("Informe a senha da conta: ")
        except ValueError as e:
            print(30 * "#")
            print("\033[1m\033[31mErro:", e, "\nTente novamente!\033[0m")
            print(30 * "#")
            ID = input("Informe o ID da conta: ")
            senha = int(input("Informe a senha da conta: "))
        for i in range(len(Usuario.usuarios)):
            if ID == Usuario.usuarios[i]["ID Conta"] and senha == Usuario.usuarios[i]["Senha"]:
                print("\n")
                print(f"{30 * '#'}\n")
                print(Usuario.usuarios[i]["Instancia"])
                print(f"\n{30 * '#'}")
            else:
                print(f"\n{30 * '#'}")
                print("\033[1m\033[31mErro:", "Usuário ou senha incorretos.", "\nTente novamente!\033[0m")
                print(30 * "#")

    # Sair
    elif opcao == "q":
        usuario.sair()
        break
    else:
        print("Operação inválida. Tente novamente.")
