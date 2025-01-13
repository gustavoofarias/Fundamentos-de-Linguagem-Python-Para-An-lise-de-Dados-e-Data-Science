'''
Exercício Python 093: 
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
aproveitamento = {}

aproveitamento['nome'] = input("Digite o nome do jogador: ")
aproveitamento['partidas'] = int(input("Quantas partidas jogou: "))

gols_por_partida = []
total_gols = 0

for partida in range(aproveitamento['partidas']):
    gols = int(input(f"Quantos gols {aproveitamento['nome']} fez na partida {partida + 1}: "))
    gols_por_partida.append(gols)
    total_gols += gols

aproveitamento['gols_por_partida'] = gols_por_partida
aproveitamento['total_gols'] = total_gols

print("\nDados do jogador:")

# Iterando sobre os itens do dicionário aproveitamento
for chave, valor in aproveitamento.items():
    if chave == 'nome':
        print(f"Nome do jogador: {valor}")
    elif chave == 'partidas':
        print(f"Quantidade de partidas jogadas: {valor}")
    elif chave == 'gols_por_partida':
        print("Gols feitos em cada partida:")
        for partida, gols in enumerate(valor, start=1):
            print(f"   Partida {partida}: {gols} gols")
    elif chave == 'total_gols':
        print(f"Total de gols feitos durante o campeonato: {valor}")


