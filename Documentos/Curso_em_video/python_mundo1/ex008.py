'''
Exercício Python 8:
 Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

metros = float(input("Quantos metros:"))

centimetros = metros * 100

milimetros = metros * 1000

print(f"Convertendo para centímetros é {centimetros}..")
print(f"Convertendo para milímetros é {milimetros}.")