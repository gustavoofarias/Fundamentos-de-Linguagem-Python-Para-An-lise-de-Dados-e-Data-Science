'''
Exercício Python 17:
 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''
from math import sqrt

cateto_oposto = float(input("Digite um número:"))
cateto_adjacente = float(input("Digite um número:"))


hipotenusa = sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)


print(f"O valor da hipotenusa é {hipotenusa}")


