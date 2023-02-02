km = float(input('Quantos km rodou?'))
dias = float(input('Quantos dias alugado?'))
rsk = km*0.15
rsd = dias*60
print(f'O aluguel do carro fica R${rsk+rsd:.2f}, sendo\nR${rsk:.2f} pela distância e\nR${rsd:.2f} por dias')
