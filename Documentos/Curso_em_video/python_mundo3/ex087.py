'''
Exercício Python 087: 
Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.                                                                                                  
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.
'''

# Criando uma matriz 3x3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_coluna = 0
maior_valor_segunda_linha = None

# Preenchendo a matriz com valores lidos pelo teclado
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para [{i},{j}]: "))
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
        if j == 2:
            soma_coluna += matriz[i][j]
        if i == 1:
            if maior_valor_segunda_linha is None or matriz[i][j] > maior_valor_segunda_linha:
                maior_valor_segunda_linha = matriz[i][j]

print("Matriz 3x3:")
for linha in matriz:
    for elemento in linha:
        print(f"[{elemento:^5}]", end="")
    print()  # Quebra de linha para imprimir a próxima linha

print(f"A) A soma de todos os valores pares é: {soma_pares}")
print(f"B) A soma dos valores da terceira coluna é: {soma_coluna}")
print(f"C) O maior valor da segunda linha é: {maior_valor_segunda_linha}")
