'''
Exercício Python 50: 
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o.
'''
lista = []

for i in range(1,7):
    num = int(input("Digite um número:"))
    if num % 2 == 0:
        lista.append(num)
soma = sum(lista)

print(f"A soma dos números pares é {soma}")

    


