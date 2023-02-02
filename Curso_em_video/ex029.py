v = int(input('Qual a velocidade do carro? '))
if v > 80:
    m = (v-80)*7
    print(f'Você está acima do limite e foi multado em R${m:.2f}.')
else:
    print('parabéns, você está dentro do limite!')
