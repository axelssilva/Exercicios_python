from datetime import date
atual = date.today().year
nasc = int(input('Em que ano nasceu?'))
idade = atual-nasc
if idade < 9:
    print(f'Voce tem {idade} anos, sua classificação é MIRIM')
elif 9 < idade < 14:
    print(f'Voce tem {idade} anos, sua classificação é INFANTIL')
elif 14 < idade < 19:
    print(f'Voce tem {idade} anos, sua classificação é JÚNIOR')
elif 19 < idade < 25:
    print(f'Voce tem {idade} anos, sua classificação é SÊNIOR')
else:
    print(f'Voce tem {idade} anos, sua classificação é MASTER')
