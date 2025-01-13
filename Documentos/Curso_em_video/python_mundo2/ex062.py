'''
Exercício Python 62: 
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''
while True:
    primeiro_termo = int(input("Digite o primeiro termo da PA: "))
    razao = int(input("Digite a razão da PA: "))
    contador = 0  # Iniciar o contador em 0

    while contador < 10:  # Executar o loop enquanto o contador for menor que 10
        termo_atual = primeiro_termo + contador * razao
        print(termo_atual, end=" ")
        contador += 1  # Incrementar o contador após cada iteração
        termos = input("Você quer ver mais termos? Sim ou Não").upper()

        if termos == "SIM":
            continue
        elif termos == "NÂO" or termos == "0":
            break
        
    
    
