'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
lista_par = []
lista_impar = []

print("Digite os números. Digite um número negativo para encerrar.")

while True:
    num = int(input("Digite um número: "))

    if num < 0:
        break
    else:
        lista.append(num)

for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print("Lista completa:", lista)
print("Lista de números pares:", lista_par)
print("Lista de números ímpares:", lista_impar)
