from datetime import date
atual = date.today().year
nasc = int(input('Em que ano nasceu? '))
idade = atual - nasc
pas = idade-18
vem = 18-idade
if idade == 18:
    print(f'Você tem {idade} anos e deve se alistar imediatamente!')
elif idade > 18:
    print(f'Sua idade é {idade} anos, seu alistamento já passou ({atual-pas})')
else:
    print(f'Sua idade é {idade} anos e vai se alisatar futuramente ({atual+vem})')
