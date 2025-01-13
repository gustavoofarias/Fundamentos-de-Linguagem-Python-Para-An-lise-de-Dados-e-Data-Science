'''
Exercício Python 25: 
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
'''

nome = input("Digite seu nome:")
split_nome = nome.upper().split()
tem_silva = False
for parte_nome in split_nome:
    if parte_nome == "SILVA":
        tem_silva = True
        break  

if tem_silva:
    print("O nome tem SILVA.")
else:
    print("O nome não tem SILVA.")
