valor = float(input('Valor do produto: '))
método = int(input('''Escolha uma opção
[1] à vista/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão
opção: '''))
if método == 1:
    print(f'Você tem 10% de desconto, o valor ficou R${valor-(valor*10)/100:.2f}')
elif método == 2:
    print(f'Você tem 5% de desconto, o valor ficou R${valor-(valor*5)/100:.2f}')
elif método == 3:
    print(f'Você não tem desconto, o valor ficou 2 x de R${valor/2:.2f}')
elif método == 4:
    vezes = int(input('Quantas vezes?'))
    print(f'Você tem juros de 20 %, o valor ficou {vezes} x de R${(valor+(valor*20)/100)/vezes:.2f}')
else:
    print('Opção invalida')