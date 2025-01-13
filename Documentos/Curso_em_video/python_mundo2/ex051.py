'''
Exercício Python 51: 
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
mostre os 10 primeiros termos dessa progressão.
'''


primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

print("Os 10 primeiros termos da progressão aritmética são:")

# Calcula e exibe os 10 primeiros termos da PA
for i in range(10):
    termo_atual = primeiro_termo + i * razao
    print(termo_atual, end=" ")
