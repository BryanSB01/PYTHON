# Inicializa uma lista vazia chamada 'itens'.
itens = []

# Itera sobre um intervalo de valores de 0 a 2 (3 valores no total).
for i in range(3):
    # Solicita que o usuário insira um item e armazena o valor na variável 'item'.
    item = input()
    # Adiciona o item à lista 'itens'.
    itens.append(item)

# Imprime um cabeçalho indicando que a lista de equipamentos será exibida.
print("Lista de Equipamentos:")

# Itera sobre cada item na lista 'itens'.
for item in itens:
    # Imprime cada item precedido por um traço, formatando a saída com uma f-string.
    print(f"- {item}")
