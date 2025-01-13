'''
Exercício Python 4: 
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

entrada = input("Digite algo:")

tipo_primitivo = type(entrada)

print(tipo_primitivo)

if tipo_primitivo == str:
    print("É uma string")

elif tipo_primitivo == int:
    print("É um número inteiro.")

elif tipo_primitivo == float:
    print("É um número flutuante.")

elif tipo_primitivo == bool:
    print("É tipo primitivo booleano")

