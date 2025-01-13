'''
Exercício Python 39: 
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

ano_nascimento = int(input("Digite seu ano de nascimento:"))
ano_atual = 2024
idade = ano_atual - ano_nascimento

if idade > 18:
    print("Já passou da hora de se alistar.")
    anos_passados = idade - 18
    print(f"Já passou {anos_passados} anos para se alistar.")

elif idade < 18:
    print("Ainda fata tempo para tu se alistar")
    anos_restantes = 18 - idade
    print(f"Falta {anos_restantes} anos para você se alistar.")

elif idade == 18:
    print("Está na hora de se alistar.")



