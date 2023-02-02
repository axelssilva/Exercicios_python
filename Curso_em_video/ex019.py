import random
a1 = input('1° Aluno: ')
a2 = input('2° Aluno: ')
a3 = input('3° Aluno: ')
a4 = input('4° Aluno: ')
lista = [a1, a2, a3, a4]
print(f'Os alunos a serem sorteados são: {lista}')
sorteado = random.choice(lista)
print(f'O sorteado foi: {sorteado}')
