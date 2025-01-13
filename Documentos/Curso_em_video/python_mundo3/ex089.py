'''
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

lista_notas = []

while True:
    lista_temp = []

    nome = str(input("Digite o nome do aluno: "))
    lista_temp.append(nome)
    nota1 = float(input("Digite a primeira nota: "))
    lista_temp.append(nota1)
    nota2 = float(input("Digite a segunda nota: "))
    lista_temp.append(nota2)

    lista_notas.append(lista_temp[:])
    lista_temp.clear()

    usuario = input("Deseja continuar cadastrando alunos? (S/N): ").upper()

    if usuario != 'S':
        break

print("Boletim:")

for aluno in lista_notas:
    nome = aluno[0]
    media = (aluno[1] + aluno[2]) / 2
    print(f"Nome: {nome}")
    print(f"Média do aluno: {media:.2f}")
    print()

while True:
    aluno_desejado = input("Qual aluno você deseja ver as notas? (Digite o nome ou 'sair' para encerrar): ")
    
    if aluno_desejado.lower() == 'sair':
        break
    
    encontrado = False
    for aluno in lista_notas:
        if aluno_desejado.lower() == aluno[0].lower():
            print(f"Notas de {aluno[0]}: {aluno[1]}, {aluno[2]}")
            encontrado = True
            break
    
    if not encontrado:
        print("Aluno não encontrado.")
