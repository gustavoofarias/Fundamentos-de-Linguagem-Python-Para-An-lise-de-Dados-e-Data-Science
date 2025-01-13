'''
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
'''

tabela_brasileirao = (
    "Fluminense",
    "Palmeiras",
    "São Paulo",
    "Corinthians",
    "Grêmio",
    "Internacional",
    "Atlético Mineiro",
    "Botafogo",
    "Santos",
    "Athletico Paranaense",
    "Cruzeiro",
    "Chapecoense",
    "Bahia",
    "Goiás",
    "Fortaleza",
    "Ceará",
    "Sport",
    "Coritiba",
    "Bragantino",
    "Flamengo"
)

a = tabela_brasileirao[0:6]
b = tabela_brasileirao[-5:]
c = sorted(tabela_brasileirao)
d = tabela_brasileirao.index("Chapecoense")

print(f"Os primeiros times: {a}")
print(f"Os últimos são: {b}")
print("-" * 100)
print("Em ordem albetica:")
print(c)
print("-" * 100)
print(f"A chapecoense está no indice: {d}")
