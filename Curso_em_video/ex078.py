lista = list()
for c in range(1,6):
    n = int(input('Digite um número: '))
    lista.append(n)
menor = min(lista)
maior = max(lista)
print(f'''Sua lista é:
{lista}
O maior número é {maior} na posição {lista.index(maior)}
O menor número é {menor} na posição {lista.index(menor)}''')
