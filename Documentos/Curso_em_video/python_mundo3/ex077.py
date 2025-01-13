'''
Exercício Python 077: 
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

# Definindo a tupla com as palavras
palavras = ('python', 'programacao', 'computador', 'algoritmo', 'linguagem')

# Iterando sobre cada palavra na tupla e mostrando suas vogais
for palavra in palavras:
    vogais = [letra for letra in palavra if letra in 'aeiou']
    print(f'Vogais em "{palavra}": {vogais}')
