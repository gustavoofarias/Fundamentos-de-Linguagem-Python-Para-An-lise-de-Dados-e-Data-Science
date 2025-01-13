'''
Exercício Python 106: 
Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.



'''

import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 'blue')
    print(Fore.GREEN, end='')
    help(comando)

def titulo(msg, cor='none'):
    cores = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'none': ''
    }
    tam = len(msg) + 4
    print(cores[cor] + '~' * tam)
    print(cores[cor] + f'  {msg}')
    print(cores[cor] + '~' * tam)

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 'yellow')
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 'red')
