from random import randint
num = randint(1, 10)
jogador = int(input('''Pensei em um número entre 1 e 10, você consegue adivinhar? 
Palpite: '''))
while jogador != num:
    if jogador < num:
        jogador = int(input('''Hmm... ainda não, um pouco mais
Palpite: '''))
    elif jogador > num: 
        jogador = int(input('''Hmm... ainda não, um pouco menos
Palpite: '''))
print(f'o número era {num}, você acertou, parabéns')
