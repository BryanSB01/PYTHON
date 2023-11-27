from random import randint

def geralista(tamanho, vMin=0, vMax=10):
    L = []
    for i in range(tamanho):
        n = randint(vMin, vMax)
        while n in L:
            n = randint(vMin, vMax)
        L.append(n)
    return L

def selectionSort(Lista):
    for j in range(len(Lista)-1):
        indiceMenor = j
        for i in range(j, len(Lista)):
            if Lista[i] < Lista[indiceMenor]:
                indiceMenor = i
    
        if Lista[j] > Lista[indiceMenor]:
            Lista[j], Lista[indiceMenor] = Lista[indiceMenor], Lista[j]
    
    return Lista

nums = geralista(10)

print(nums)
print(selectionSort(nums))