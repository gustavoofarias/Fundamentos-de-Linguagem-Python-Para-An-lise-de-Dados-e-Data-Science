'''
Exercício Python 47: 
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

'''

lista = []
for contador in range(1,51):
    contador += 1
    if contador % 2 == 0:
        lista.append(contador)

print("Os números pares no no intervalo de 1 e 50")
print(lista)

    