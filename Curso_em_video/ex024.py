cida = str(input('Digite o nome da sua cidade: '))
cm = cida.upper().split()
sn = 'SANTO' in cm[0]
print(f'Começa com santo? {sn}')
