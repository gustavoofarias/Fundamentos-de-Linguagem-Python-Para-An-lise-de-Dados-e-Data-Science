'''
Exercício Python 23: 
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''

numero = int(input("Digite um número:"))

print(f"O número é {numero}")

if numero >= 0 and numero <= 9999:
    string = str(numero)
    unidade = int(string[-1])
    print(f"Esse número possui: {unidade} unidades.")
    dezenas = int(string[-2])
    print(f"Esse número possui: {dezenas} dezenas.")
    centenas = int(string[1])
    print(f"Esse número possui: {centenas} centenas.")
    milhares = int(string[0])
    print(f"Esse número possui: {milhares} milhares.")

else:
    print("Número inválido.")
