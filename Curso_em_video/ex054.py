from datetime import date
atual = date.today().year
maioridade = 0
menoridade = 0
for p in range(1,8):
    nasc = int(input(f'Ano de nascimento {p} pessoa: '))
    if atual - nasc > 21:
        maioridade += 1
    elif atual - nasc < 21:
        menoridade += 1
print(f'{maioridade} das pessoas são maiores de idade e\n{menoridade} das pessoas são menores de idade')
