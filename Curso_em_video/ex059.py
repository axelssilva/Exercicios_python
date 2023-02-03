n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
resposta = 0 
while resposta !=5:
    resposta = int(input('''Escolha uma opção:
[1] somar
[2] multiplicar
[3] maior 
[4] novos valores 
[5] sair do programa
=======================
Escolha: '''))
    if resposta == 1: 
        print(f'A soma entre {n1} e {n2} é igual a {n1+n2}')
    elif resposta == 2:
        print(f'O produto entre {n1} e {n2} é igual a {n1*n2}')
    elif resposta == 3:
        if n1 > n2:
            print(f'O primeiro é maior')
        elif n2 > n1:
            print(f'O segundo é maior')
        else:
            print(f'Ambos são iguais')
    elif resposta == 4:
        n1 = int(input('''Novos valores
----------------------
Digite um valor: '''))
        n2 = int(input('Digite outro valor: '))
    elif resposta == 5:
        print('obrigado, até logo')
    else:
        print('''Comando inválido, tente novamente:''')

