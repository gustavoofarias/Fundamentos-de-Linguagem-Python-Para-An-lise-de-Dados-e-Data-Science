'''
Exercício Python 104: 
Crie um programa que tenha a função leiaInt(), 
que vai funcionar de forma semelhante ‘a função input() do Python,
 só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

'''

def leiaint(num):
    if not isinstance(num, int):
        print("Não é um valor inteiro!")

    else:
        print("É um valor inteiro.")

    return num


num = leiaint(5.2)

print(f"Você digitou o número: {num}")