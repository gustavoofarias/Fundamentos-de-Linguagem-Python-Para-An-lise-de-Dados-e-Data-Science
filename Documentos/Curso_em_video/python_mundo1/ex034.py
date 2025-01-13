'''
Exercício Python 34: 
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, o aumento é de 15%.

'''

salario = float(input("Digite seu salário:"))

if salario > 1250:
    aumento = salario + (salario * 0.10) 
    print(f"Você recebeu um aumento de {aumento}R$")

elif salario <= 1250:
    aumento = salario + (salario * 0.15)
    print(f"Você recebeu um aumento de {aumento}R$")


