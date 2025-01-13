'''
Exercício Python 059: 
Crie um programa que leia dois valores e mostre um menu na tela:
'''
while True:
    valor1 = int(input("Digite o primeiro número: "))
    valor2 = int(input("Digite o segundo número: "))

    while True:
        menu = int(input('''
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
        
        Escolha uma opção: '''))

        if menu == 1:
            resultado = valor1 + valor2
            print(f"A soma dos valores é {resultado}")

        elif menu == 2:
            resultado = valor1 * valor2
            print(f"A multiplicação dos valores é {resultado}")

        elif menu == 3:
            if valor1 > valor2:
                print(f" O maior valor é {valor1}")
            elif valor1 == valor2:
                print("Os valores são iguais.")
            else:
                print(f"O valor {valor2} é maior.")

        elif menu == 4:
            break  # Sai do loop interno para pedir novos números.

        elif menu == 5:
            print("Você saiu do programa!")
            quit()  # Encerra o programa.

    # O loop continua a solicitar novos números enquanto o usuário escolhe a opção "novos números".
