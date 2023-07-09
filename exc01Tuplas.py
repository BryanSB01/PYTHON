numeros = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número de 0 a 20\n'))
while num < 0 or num > 20:
    print("Número fora do intervalo. Tente novamente.")
    num = int(input('Digite um número de 0 a 20\n'))    
for pos, n in enumerate(numeros):
    if num == pos:
        print(f"Você digitou o número: {n}")