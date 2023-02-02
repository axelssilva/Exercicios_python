soma = 0
contador = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma += num
        contador +=  1
print(f'A soma entre os {contador} números é {soma}')
