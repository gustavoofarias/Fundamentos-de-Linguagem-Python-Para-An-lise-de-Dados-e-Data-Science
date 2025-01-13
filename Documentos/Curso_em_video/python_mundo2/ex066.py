'''
Exercício Python 66: 
Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

'''

numeros = []
contador = 0
while True:
    numero = int(input("Digite um número: "))
    if numero == 999:
        break
    numeros.append(numero)
    contador += 1

soma = sum(numeros)
print(f"A soma dos números foi {soma}")
print(f"A quantidade de números que foi digitada é {contador}")
