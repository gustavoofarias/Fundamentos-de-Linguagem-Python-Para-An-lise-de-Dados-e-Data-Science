'''
Exercício Python 092: 
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
lista = []

while True:
    dicionario = {}  # Move a criação do dicionário para dentro do loop
    nome = input("Digite seu nome: ")
    dicionario['nome'] = nome
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    dicionario['ano_nascimento'] = ano_nascimento
    carteira = input("Você tem carteira de trabalho? [S/N]").upper()

    if carteira == "S":
        carteira_trabalho = int(input("Digite sua carteira de trabalho: "))
        if carteira_trabalho != 0:
            dicionario['carteira_trabalho'] = carteira_trabalho
            ano_contratação = int(input("Qual o seu ano de contratação: "))
            dicionario['ano_contratação'] = ano_contratação
            idade = 2024 - ano_nascimento
            dicionario['idade'] = idade
            salario = float(input("Qual é o seu salario: "))
            dicionario['salario'] = salario

            anos_contribuicao = 2024 - ano_contratação
            idade_aposentadoria = idade + (35 - anos_contribuicao)
            dicionario['idade_aposentadoria'] = idade_aposentadoria
    else:
        print("Você não possui carteira de trabalho.")

    lista.append(dicionario)

    continuar = input("Você deseja continuar? [S/N]").upper()

    if continuar != 'S':
        print("Finalizando...")
        break

print(lista)
