from collections import deque

lista = deque(["Pão", "Arroz", "Feijão"])
lista.append("54")
print(lista)
lista.popleft()
lista.pop()
print(lista)