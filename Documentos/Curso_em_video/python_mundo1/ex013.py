'''
Exercício Python 13: 
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

'''

salario = float(input("Digite seu salário:"))

aumento = salario * 0.15

novo_salario = salario + aumento

print(f"O novo salário é {novo_salario}")

