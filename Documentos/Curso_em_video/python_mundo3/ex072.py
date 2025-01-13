'''
Exercício Python 72: 
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

'''
numeros_por_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete","dezoito", "dezenove", "vinte")

numero_digitado = int(input("Digite um número entre 0 e 20: "))

if 0 <= numero_digitado <= 20:
    print(f"O número digitado por extenso é: {numeros_por_extenso[numero_digitado]}")
else:
    print("Número fora do intervalo válido.")

