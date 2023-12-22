import pandas as pd #Importa a biblioteca Pandas para manipulação do dataset;
import plotly.express as px #Importa a biblioteca Plotly para plotar no mapa os dados do dataset;

dicio = {} #Cria um dicionário "dicio" vazio.
vaccines = {} #Cria um dicionário "vaccines" vazio.

data = pd.read_csv("covid19.csv") #A variável "data" recebe a tabela contida no arquivo csv e converte para "Data Frame".;

cv = data[["country","vaccines"]] #A variável cv recebe as colunas "country" e "vaccines" da tabela;

for i in cv.vaccines.unique(): #Para cada grupo único de vacinas;
    dicio[i] = [cv["country"][j] for j in cv[cv["vaccines"]==i].index] #Se o grupo de vacinas for igual ao grupo único de vacinas, o dicionário recebe o grupo de vacinas e a lista países que a possuem;

for key, value in dicio.items(): #Para cada chave e valores do dicionário "dicio";
    vaccines[key] = set(value) #Inclua no dicionário "vaccines" a chave e os valores únicos de "dicio";

#Visualização no terminal:
for key, value in vaccines.items():
    print(50*"=--=")
    print(f"\nVacinas: {key}")
    print(f"Países: ", end='')
    for p in value:
        print(f"{p}", end=' | ')
    print("\n")

#Mostrando os dados em Mapa Coroplético:
vaccine_map = px.choropleth(data, locations = "iso_code", color = "vaccines", title="Vacinas Covid-19 Mundo") #Cria um mapa coroplético a partir do data
vaccine_map.update_layout(height=400, margin={"r":0,"t":50,"l":50,"b":0})
#vaccine_map.show() 