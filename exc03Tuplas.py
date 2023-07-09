from random import randrange
numeros = (randrange(10), randrange(10), randrange(10), randrange(10), randrange(10))
print(f"Os valores sorteados foram {numeros}")
print(f"O maior valor sorteado foi {max(numeros)}")
print(f"O menor valor sorteado foi {min(numeros)}")