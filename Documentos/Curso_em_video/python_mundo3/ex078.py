'''
Exercício Python 078: 
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

lista = []


for i in range(5):
    numeros = int(input("Digite um número:"))
    lista.append(numeros)

min = min(lista)
max = max(lista)

pos_menor = lista.index(min)
pos_maior = lista.index(max)

print(f"O menor valor foi {min} e sua posição é {pos_menor }")
print(f"O maior valor foi {max} e sua posição é {pos_maior }")

