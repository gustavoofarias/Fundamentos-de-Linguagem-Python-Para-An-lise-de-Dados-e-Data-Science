'''
Exercício Python 105: Faça um programa que tenha uma função notas()
 que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas  – A maior nota  – A menor nota – A média da turma – A situação (opcional)
'''

def notas(list=[]):
    maior_nota = max(list)
    print(f"A maior nota é {maior_nota}")
    menor_nota = min(list)
    print(f"A menor nota é {menor_nota}")
    media_turma = sum(list) / len(list)
    print(f"A média da turma é {media_turma}")



lista = [9.7, 4.5,7.5, 4.7, 8.6, 7,6]

notas(lista)