n = int(input('Digite um número: '))
t = int(input('''Escolha uma opção
[1] binario
[2] octa
[3] hexadecimal
desejado: '''))
if t == 1:
    print(f'Em binario é {bin(n)[2:]}')
elif t==2:
    print(f'Em octa é {oct(n)[2:]}')
elif t==3:
    print(f'Em hexadecimal é {hex(n)[2:]}')
else:
    print('Comando invalido')
