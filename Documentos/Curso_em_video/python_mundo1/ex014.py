'''
Exercício Python 14:
 Escreva um programa que converta uma temperatura digitando em graus Celsius e converta
   para graus Fahrenheit.
'''

graus_celsius = float(input("Digite quantos graus está a temperatura:"))


fahrenheit = (graus_celsius * 9/5) + 32


print(f"A conversão de {graus_celsius} graus celsius para fahrenheit é {fahrenheit}")