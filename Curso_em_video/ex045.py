from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print('=-'*10)
jog = int(input('''Suas opções são
[0] Pedra
[1] Papel
[2] Tesoura
sua escolha: '''))
print('=-'*10)
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA!!')
print(f'O computador jogou {(itens[pc])} você jogou {(itens[jog])}')
if pc == 0:
    if jog == 0:
        print('Empate')
    elif jog == 1:
        print('Jogador ganhou')
    elif jog == 2:
        print('Pc ganhou')
    else:
        print('Jogada invalida')
elif pc == 1:
    if jog == 0:
        print('PC ganhou')
    elif jog == 1:
        print('Empate')
    elif jog == 2:
        print('Jogador ganhou')
    else:
        print('Jogada invalida')
elif pc == 2:
    if jog == 0:
        print('Jogador ganhou')
    elif jog == 1:
        print('PC ganhou')
    elif jog == 2:
        print('Empate')
    else:
        print('Jogada invalida')
