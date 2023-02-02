import random
print('Vamos jogar, vou pensar em um número de 0 a 5 e você tenta descobrir')
n = random.randint(0,5)
print('hmmmm, já pensei')
m = int(input('Digite um número: '))
if m == n:
    print('Você ganhou, PARABENS!!')
else:
    print('Você perdeu :(')
print('--Fim--')
