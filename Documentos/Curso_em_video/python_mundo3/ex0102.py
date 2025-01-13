'''
Exercício Python 102: 
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


'''

def fatorial_iterativo(n):
    if n < 0:
        return "Fatorial não definido para números negativos"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(fatorial_iterativo(5))  # Saída: 120
