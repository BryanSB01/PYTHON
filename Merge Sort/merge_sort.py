import random, time

def merge_sort(lista, inicio=0, fim=None):
  if fim == None:
    fim = len(lista)

  if (fim - inicio) > 1:
    meio = (fim + inicio) // 2
    merge_sort(lista, inicio, meio)
    merge_sort(lista, meio, fim)
    merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
  esquerda = lista[inicio:meio]
  direita = lista[meio:fim]

  topo_esquerda = 0
  topo_direita = 0

  for k in range(inicio, fim):
    if topo_esquerda >= len(esquerda):
      lista[k] = direita[topo_direita]
      topo_direita += 1

    elif topo_direita >= len(direita):
      lista[k] = esquerda[topo_esquerda]
      topo_esquerda += 1

    elif esquerda[topo_esquerda] < direita[topo_direita]:
      lista[k] = esquerda[topo_esquerda]
      topo_esquerda += 1

    else:
      lista[k] = direita[topo_direita]
      topo_direita += 1


L1 = [x for x in range(1,10)]
random.shuffle(L1)
print(f"{60 * '#'}\n")
print("Lista 1: Intervalo 1:10\n")
print(f"Lista L1 Desordenada: {L1}")
inicio1 = time.time()
merge_sort(L1)
fim1 = time.time()
tempo1 = fim1 - inicio1
print(f"Lista L1 Ordenada: {L1}\n")
print(f"Tempo de Execução: {tempo1} segundos\n\n")

L2 = [x for x in range(1,100)]
random.shuffle(L2)
print(f"{60 * '#'}\n")
print("Lista 2: Intervalo 1:100\n")
print(f"Lista L2 Desordenada: {L2}\n")
inicio2 = time.time()
merge_sort(L2)
fim2 = time.time()
tempo2 = fim2 - inicio2
print(f"Lista L2 Ordenada: {L2}\n")
print(f"Tempo de Execução: {tempo2} segundos\n")
print(f"{60 * '#'}\n")

L3 = [x for x in range(1,1000000)]
random.shuffle(L3)
print(f"{60 * '#'}\n")
print("Lista 3: Intervalo 1:1000000\n")
inicio3 = time.time()
merge_sort(L3)
fim3 = time.time()
tempo3 = fim3 - inicio3
print(f"Tempo de Execução: {tempo3:.6f} segundos\n")
print(60 * "#")
