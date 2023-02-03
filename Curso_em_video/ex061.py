razão = int(input('Razão: '))
pt = int(input('Primeiro termo: '))
termo = pt
cont = 0
while cont != 10:
    cont += 1
    termo += razão
    print(termo, end= '-')
print('fim')
