'''
Exercício Python 079: 
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

lista = []

for num in range(5):
    num = int(input("Digite um número:"))

    if num in lista:
        continue
    else:
        lista.append(num)

print(sorted(lista))

    