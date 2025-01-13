'''
Exercício Python 076: 
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

produtos_precos = (
    "Camiseta", 29.99,
    "Calça Jeans", 49.99,
    "Tênis", 79.99,
    "Relógio", 99.99,
    "Mochila", 39.99
) 

for pos in range(0, len(produtos_precos)):
    if pos % 2 == 0:
        print(f"{produtos_precos[pos]:.<30}", end="")

    else:
        print(f"{produtos_precos[pos]:>7.2f}")
