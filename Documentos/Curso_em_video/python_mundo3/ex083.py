'''
Exercício Python 083: 
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

expressao = input("Digite uma expressão contendo parênteses: ")

pilha = []

for char in expressao:
    if char == '(':
        pilha.append('(')
    elif char == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print("Expressão válida: os parênteses estão corretamente balanceados.")
else:
    print("Expressão inválida: os parênteses não estão balanceados corretamente.")
