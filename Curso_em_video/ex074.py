from random import randint
num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10),)
print(f'sorteei os números {num}')
maior = 0
menor = 0
for c in range(0, 5):
    if c == 0:
        maior = num[c]
        menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print(f'O maior é {maior}\nE o menor é {menor}')
