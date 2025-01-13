'''
Exercício Python 18:
 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, 
 cosseno e tangente desse ângulo.
'''
import math

angulo = float(input("Digite o ângulo:"))


seno = math.sin(angulo)
conseno = math.cos(angulo)
tangente  = math.tan(angulo)


print(f"O seno é {seno}")
print(f"O conseno é {conseno}")
print(f"A tangente é {tangente}")


