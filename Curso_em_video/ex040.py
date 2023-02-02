n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1+n2)/2
if média < 5:
    print(f'Sua media foi {média:.1f} você está reprovado')
elif 5 < média < 6.9:
    print(f'Sua média foi {média:.1f} você está em recuperação')
else:
    print(f'Sua média foi {média:.1f} você foi aprovado, parabéns')
