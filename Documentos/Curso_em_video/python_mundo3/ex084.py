'''
Exercício Python 084: 
Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. 
No final, mostre:                                                                                                    
A) Quantas pessoas foram cadastradas.                                                                                                                
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.
'''
lista = []


for i in range(5):
    
    temp_lista = []
    temp_lista.append(str(input("Digite seu nome: ")))
    temp_lista.append(float(input("Digite seu peso: ")))
    lista.append(temp_lista[:])
    temp_lista.clear()

pessoas_mais_pesadas = max(lista, key=lambda x: x[1])
pessoas_mais_leves = max(lista, key=lambda x: x[1])

print(pessoas_mais_pesadas)


print(lista)
