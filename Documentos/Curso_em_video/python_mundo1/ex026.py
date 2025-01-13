'''
Exercício Python 26: 
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

frase = str(input("Digite uma frase:")).upper().strip()

print(f"A letra A aparece {frase.count('A')} vezes.")
print(f"A primeira fez que apareceu a Letra A foi na posição {frase.find('A') + 1}")
print(f"A última pisição a aparecer a Letra A foi {frase.rfind('A') + 1}")




