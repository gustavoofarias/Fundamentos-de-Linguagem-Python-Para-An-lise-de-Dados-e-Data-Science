'''
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.
'''
lista_par = []
lista_impar = []

for i in range(7):
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print(f"Os números pares em ordem são: {sorted(lista_par)}")
print(f"Os números ímpares em ordem são: {sorted(lista_impar)}")


