'''
Exercício Python 48: 
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
lista = []
for i in range(1,501):
    if i % 3 == 0:
        lista.append(i)
soma = sum(lista)

print(f"A soma de todos os multíplos de 3 é {soma}.")