# Define a função 'recomendar_plano' que recebe como parâmetro 'consumo', que representa a quantidade de dados consumidos.
def recomendar_plano(consumo):
    # Verifica se o consumo é menor ou igual a 10.
    if consumo <= 10:
        # Retorna a string indicando o plano recomendado se o consumo for menor ou igual a 10.
        return "Plano Essencial Fibra - 50Mbps"
    # Verifica se o consumo está entre 10 e 20.
    elif consumo > 10 and consumo <= 20:
        # Retorna a string indicando o plano recomendado se o consumo estiver entre 10 e 20.
        return "Plano Prata Fibra - 100Mbps"
    # Se o consumo for maior que 20 (não precisa verificar explicitamente se é maior que 10, pois essa condição seria verdadeira se não fosse atendida pelas condições anteriores).
    elif consumo > 20:
        # Retorna a string indicando o plano recomendado se o consumo for maior que 20.
        return "Plano Premium Fibra - 300Mbps"

# Solicita que o usuário insira o consumo, convertendo-o para ponto flutuante.
consumo = float(input())

# Chama a função 'recomendar_plano' com o valor inserido pelo usuário e imprime o resultado.
print(recomendar_plano(consumo))
