'''
Exercício Python 35: 
Desenvolva um programa que leia o comprimento de três retas
 e diga ao usuário se elas podem ou não formar um triângulo.
'''

a = float(input("Digite o comprimento da reta:"))
b = float(input("Digite o comprimento da reta:"))
c = float(input("Digite o comprimento da reta:"))


if a + b > c and a + c > b and b + c > a:
    print("Pode formar um triangulo.")

else:
    print("Não pode formar um triangulo.")