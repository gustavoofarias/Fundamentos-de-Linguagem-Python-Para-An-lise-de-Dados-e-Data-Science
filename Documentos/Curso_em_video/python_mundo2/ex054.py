'''
Exercício Python 54: 
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

'''


maior_de_idade = 0
menor_de_idade = 0
for i in range(7):
    ano_nascimento = int(input("Digite o ano do seu nascimento:"))
    if 2024 - ano_nascimento >= 18:
        maior_de_idade += 1

    elif 2024 - ano_nascimento < 18:
        menor_de_idade += 1

print(f"Tem {maior_de_idade} pessoas maiores de idade.")
print(f"Tem {menor_de_idade} pessoas menores de idade.")
