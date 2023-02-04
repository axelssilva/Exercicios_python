num = (int(input('Digite um número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite um último número: ')))
print(f'Você digitou os valores {num}')
if 9 in num:
    print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 aparece primeiro na posição {num.index(3)+1}')
print('Os números pares encontrados foram: ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
