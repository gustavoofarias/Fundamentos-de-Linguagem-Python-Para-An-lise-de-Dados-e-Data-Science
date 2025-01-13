'''
Exercício Python 36: 
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

casa = float(input("Digite o valor da casa:"))
salario = float(input("Digite o seu salário:"))
anos = int(input("Quantos anos você vai pagar?"))

prestação = (casa / (anos * 12))
print(f"O valor da prestação é {prestação}")

if prestação <= 0.30 * salario:
    print(f"O empréstimo foi aprovado.")

else:
    print(f"O empréstimo foi negado!")



