campBra = ('Botafogo', 'Palmeiras', 'Flamengo', 'Atlético Mineiro', 'Fluminense', 'Gremio', 'Atlético Paranaense', 'São Paulo', 'Cruzeiro', 'Internacional', 'Fortaleza', 'Bragantino', 'Santos', 'Cuiabá', 'Bahia', 'Corinthians', 'Goiás', 'América', 'Vasco', 'Coritiba')
#Mostrando os 5 primeiros colocados do campeonato:
print(campBra[0:5])
#Mostrando os últimos 4 colocados do campeonato:
print(campBra[-4:])
#Mostrando os times em ordem alfabética:
print(sorted(campBra))
#Mostrando em que posição da tabela está o time do São Paulo:
print(f"O time do São Paulo está na {campBra.index('São Paulo') + 1}ª posição do campeonato brasileiro.")