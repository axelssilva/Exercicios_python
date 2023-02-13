lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print(f'O número {n} já está na lista')
    else:
        lista.append(n)
        print(f'Número {n} adicionado com sucesso')
    resp = str(input('Deseja continuar? [s/n]')).strip().upper()
    if resp in 'nN':
        break
print(f'''Sua lista é:
{sorted(lista)}''')
