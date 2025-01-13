'''
Exercício Python 040:
 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
'''

'''
Exercício Python 040:
 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
'''

primeira_nota = float(input("Digite sua nota:"))

segunda_nota = float(input("Digite sua nota:"))

media = (primeira_nota + segunda_nota) / 2

if media < 5:
    print("Você foi reprovado")

elif media > 5 and media <= 6.9:
    print("Você está de recuperação")

elif media >= 7.0:
    print("Você está aprovado!")