'''
Exercício Python 086: 
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.

'''

# Criando uma matriz 3x3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Preenchendo a matriz com valores lidos pelo teclado
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para [{i},{j}]: "))

# Mostrando a matriz na tela com a formatação correta
print("Matriz 3x3:")
for linha in matriz:
    for elemento in linha:
        print(f"[{elemento:^5}]", end="")
    print()  # Quebra de linha para imprimir a próxima linha
