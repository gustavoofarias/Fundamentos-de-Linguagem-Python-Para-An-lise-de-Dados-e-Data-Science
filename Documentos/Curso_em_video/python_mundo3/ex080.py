'''
Exercício Python 080: 
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.
'''
# Inicializa a lista vazia
lista = []

# Loop para receber cinco valores do usuário
for _ in range(5):
    valor = int(input('Digite um valor: '))

    # Se a lista estiver vazia ou o valor digitado for maior que o último elemento da lista
    # Adiciona o valor no final da lista
    if len(lista) == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        # Procura a posição correta para inserção
        for i in range(len(lista)):
            if valor <= lista[i]:
                lista.insert(i, valor)
                break

print(f'A lista ordenada é: {lista}')
