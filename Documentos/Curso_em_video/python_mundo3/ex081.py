'''
Exercício Python 081: 
Crie um programa que vai ler vários números e colocar em uma lista.                  
Depois disso, mostre:                                                                                                                                                
A) Quantos números foram digitados.                                                                                                                    
B) A lista de valores, ordenada de forma decrescente.                                                                                          
C) Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []

while True:
    print("Digite um número negativo caso queira cancelar.")
    num = int(input("Digite um número: "))
    if num < 0:
        break
    else:
        lista.append(num)

tamanho_lista = len(lista)
print(f"Foi digitado {tamanho_lista} números.")

if 5 in lista:
    print("O número 5 está presente na lista.")
else:
    print("O número 5 não está presente na lista.")

lista.sort(reverse=True)  # Ordena a lista em ordem decrescente

print("A lista em ordem decrescente:", lista)

