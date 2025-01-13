'''
Exercício Python 27: 
Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente.
'''

nome = input("Digite seu nome:").strip().split()

print(f"O primeiro nome foi {nome[0]}")
print(f"o ultimo nome foi {nome[-1]}")



