nome = str(input('Digite seu nome: '))
print(f'Seu nome é {nome}')
nome = nome.split()
print(f'Seu primeiro nome é {(nome[0])}\nSeu último nome é {(nome[len(nome)-1])}')
