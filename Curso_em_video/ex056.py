maisvelho = 0
menos20 = 0
nomemais = ''
for teste in range(1,8):
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: ').strip())
    sexo = str(input('Sexo [M/F]: '))
    print('-='*10)
    if sexo in 'Mm':
        if  idade > maisvelho:
            maisvelho = idade
            nomemais = nome
    if sexo in 'Ff':
        if idade < 20:
            menos20 += 1
print(f'O homem mais velho é {nomemais}, ele possui {maisvelho} anos\nE existem {menos20} mulheres com menos de 20 anos')
