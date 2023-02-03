num = int(input('Digite um número para saber seu fatorial: '))
cont = num
fatorial = 1
while cont > 0:
    fatorial *= cont
    cont -= 1
print(f'{num}! é {fatorial}')
