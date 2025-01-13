'''
Exercício Python 61: 
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
contador = 0  # Iniciar o contador em 0

while contador < 10:  # Executar o loop enquanto o contador for menor que 10
    termo_atual = primeiro_termo + contador * razao
    print(termo_atual, end=" ")
    contador += 1  # Incrementar o contador após cada iteração

# Não há necessidade de um "if" para verificar se o contador chegou a 10
