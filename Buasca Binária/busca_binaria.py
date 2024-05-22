def busca_binaria(lista, alvo, inicio=0, fim=None):
  if fim == None:
    fim = len(lista) - 1
  if inicio <= fim:
    elemento_meio = (fim + inicio)//2
    if alvo == lista[elemento_meio]:
      return elemento_meio
    elif alvo > lista[elemento_meio]:
      return busca_binaria(lista, alvo, elemento_meio + 1, fim)
    elif alvo < lista[elemento_meio]:
      return busca_binaria(lista, alvo, inicio, elemento_meio - 1)
  return "Elemento não encontrado"

lista_num = [-5, -2, 1, 3, 7, 10, 15, 21, 22, 25, 33, 42, 50, 80, 99]

print(busca_binaria(lista_num, -5))
print(busca_binaria(lista_num, 9))
print(busca_binaria(lista_num, 22))
print(busca_binaria(lista_num, 80))
