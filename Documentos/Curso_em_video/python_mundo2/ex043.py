'''
Exercício Python 43: 
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''
altura = float(input("Digite sua altura (em metros): "))
peso = float(input("Digite seu peso (em quilogramas): "))

IMC = peso / (altura * altura)

if IMC < 18.5:
    print("Abaixo do peso")
elif 18.5 <= IMC and IMC < 25:
    print("Peso ideal")
elif 25 <= IMC and IMC < 30:
    print("Sobrepeso")
elif 30 <= IMC and IMC < 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")
