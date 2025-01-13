'''
Exercício Python 075: 
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))
valor4 = int(input("Digite o quarto valor: "))


tupla = (valor1, valor2, valor3, valor4)
contador = 0

if tupla.index(9):
    contador += 1

print(f"Apareceu o número 9: {contador} vezes")

lista = []
for i in range(tupla):
    if i % 2 == 0:
        lista.append(i)

print(f"Os números pares foram {lista}")


b = tupla.index(3)

print(f"O número três apareceu na posição: {b}")




