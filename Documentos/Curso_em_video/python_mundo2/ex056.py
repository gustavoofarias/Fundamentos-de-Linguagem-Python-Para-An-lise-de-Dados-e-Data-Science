'''
Exercício Python 56: 
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''

# Listas para armazenar os dados das pessoas
lista_idade = []
lista_nome = []
lista_sexo = []

# Coleta os dados das pessoas
for i in range(4):
    idade = int(input("Digite sua idade: "))
    lista_idade.append(idade)
    nome = input("Digite seu nome: ").upper()
    lista_nome.append(nome)
    sexo = input("Digite seu sexo (M/F): ").upper()
    lista_sexo.append(sexo)

# Calcula a média de idade do grupo
media_idade = sum(lista_idade) / len(lista_idade)

# Encontra o homem mais velho
indice_homem_mais_velho = lista_idade.index(max(lista_idade))
nome_homem_mais_velho = lista_nome[indice_homem_mais_velho]

# Conta quantas mulheres têm menos de 20 anos
contador_mulher = sum(1 for i in range(len(lista_idade)) if lista_sexo[i] == "F" and lista_idade[i] < 20)

# Mostra os resultados
print("A média de idade do grupo é:", media_idade)
print("O homem mais velho é:", nome_homem_mais_velho)
print("Quantidade de mulheres com menos de 20 anos:", contador_mulher)


