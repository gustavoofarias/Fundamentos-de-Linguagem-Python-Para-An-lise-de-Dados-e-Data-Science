'''
Exercício Python 57:
 Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. 
 Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
while True:
    print("Digite seu sexo só M OU F.")
    sexo = input("Digite seu sexo:")

    if sexo == 'M' or sexo == 'F':
        break
    else:
        print("O valor é inválido.")
