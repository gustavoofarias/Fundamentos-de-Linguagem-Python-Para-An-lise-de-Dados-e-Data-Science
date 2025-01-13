'''
Exercício Python 55: 
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''

lista_peso = []

for i in range(5):
    peso = int(input("Digite seu peso:"))
    lista_peso.append(peso)

print(f"O menor peso foi {min(lista_peso)}")
print(f"O maior peso foi {max(lista_peso)}")