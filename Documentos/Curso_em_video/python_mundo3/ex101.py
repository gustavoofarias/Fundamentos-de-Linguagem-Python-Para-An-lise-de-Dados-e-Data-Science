'''
Exercício Python 101: 
Crie um programa que tenha uma função chamada voto()
 que vai receber como parâmetro o ano de nascimento de uma pessoa,
   retornando um valor literal indicando se uma pessoa tem voto NEGADO,
 OPCIONAL e OBRIGATÓRIO nas eleições.

'''
from datetime import datetime
from num2words import num2words

def voto(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    ano_literal = num2words(ano_nascimento, lang='pt_BR')
    
    
    if idade < 16:
        print("Você não precisa votar.")
    elif 16 <= idade < 18:
        print("Seu voto é opcional.")
    elif idade >= 18:
        print("Seu voto é obrigatório.")

    return ano_literal

# Exemplo de uso

ano_nasceu = int(input("Digite o ano que você nasceu:"))

print(f"Você nasceu em: {voto(ano_nasceu)}")



