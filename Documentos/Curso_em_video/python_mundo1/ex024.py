'''
Exercício Python 24: 
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
'''

cidade = input("Digite o nome da cidade:")

string = cidade.split()
print(f"{string}")
if string[0] == "SANTO" or string[0] == "santo" or string[0] == "Santo":
    print("Essa cidade começa com SANTO.")

else:
    print("Ela não começa com SANTO.")
     