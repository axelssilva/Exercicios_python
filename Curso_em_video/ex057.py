sexo = str(input('Digite o seu sexo: ')).upper().strip()[0]
while sexo not in 'FfMm':
    sexo = str(input('Comando inválido, inform seu sexo: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado')
