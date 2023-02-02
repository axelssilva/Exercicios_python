dis = float(input('Qual a distância? '))
if dis < 200:
    print(f'A passagem custa R${dis*0.50:.2f}')
else:
    print(f'A passagem custa R${dis*0.45:.2f}')
