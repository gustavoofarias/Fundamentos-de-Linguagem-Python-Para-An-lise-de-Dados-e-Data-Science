'''

Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''

# Inicialização das variáveis de contagem
contador_pessoas = 0
contador_homem = 0
contador_mulher = 0

# Inicialização das variáveis de contagem
contador_pessoas = 0
contador_homem = 0
contador_mulher = 0

# Inicialização das variáveis de contagem
contador_pessoas = 0
contador_homem = 0
contador_mulher = 0

# Loop infinito
while True:
    # Captura da idade e do sexo
    try:
        idade = int(input("Digite sua idade: "))
        sexo = input("Digite seu sexo (M ou F): ").upper()
    except ValueError:
        print("Por favor, digite uma idade válida.")
        continue

    # Verificação de idade e sexo
    if idade > 18:
        contador_pessoas += 1

    if sexo == "M":
        contador_homem += 1

    if sexo == "F" and idade < 20:
        contador_mulher += 1

    # Verificação se o usuário deseja continuar
    continuar = input("Deseja continuar? (SIM ou NÃO): ").upper()
    if continuar == "NÃO":
        break

# Impressão dos resultados
print(f"Existem {contador_pessoas} pessoas com mais de 18 anos.")
print(f"Foram cadastrados {contador_homem} homens.")
print(f"Existem {contador_mulher} mulheres com menos de 20 anos.")
