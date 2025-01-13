'''
Exercício Python 33: 
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

num = int(input("Digite um número:"))
num2 = int(input("Digite um número:"))
num3 = int(input("Digite um número:"))


min = min(num, num2, num3)
max = max(num,num2,num3)

print(f"O menor número é {min}")
print(f"O maior número é {max}")