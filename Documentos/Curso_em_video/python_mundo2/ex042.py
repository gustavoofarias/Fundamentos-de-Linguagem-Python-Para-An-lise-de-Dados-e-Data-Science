'''

Exercício Python 42: 
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
'''

a = float(input("Digite o comprimento da reta:"))
b = float(input("Digite o comprimento da reta:"))
c = float(input("Digite o comprimento da reta:"))


if a == b and a == c and b == c:
    print("É um triângulo equilátero.")

elif  a == b != c or a == c != b or b == c != a:
    print("É um triângulo isósceles.")

elif a != b and a != c and b != c:
    print("Esse é um triângulo Escaleno.")