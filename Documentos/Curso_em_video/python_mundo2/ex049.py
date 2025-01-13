'''
Exercício Python 49: 
Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
 só que agora utilizando um laço for.
'''
num = int(input("Digite um número:"))
multiplicador = 1
for i in range(1,11):
    tabuada = num * multiplicador
    print(f"A multiplicação de {num} x {multiplicador} é {tabuada}")
    multiplicador += 1
    
