'''
Exercício Python 67: 
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.
'''


while True:

    numero = int(input("Digite um número:"))
    
    if numero < 1:
        print("O programa foi finalizado.")

        break

    for i in range(1,11):
        tabuada = numero * i 
        print(f"{numero} x {i} = {tabuada}")


    