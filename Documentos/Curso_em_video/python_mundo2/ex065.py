'''
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

numeros = []

while True:
    print("Caso queira finalizar o programa, digite 0")
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    numeros.append(numero)

if numeros:  # Verifica se a lista não está vazia
    media = sum(numeros) / len(numeros)
    menor = min(numeros)
    maior = max(numeros)

    print(f"Média: {media}")
    print(f"Menor valor: {menor}")
    print(f"Maior valor: {maior}")
else:
    print("Nenhum número foi inserido.")
