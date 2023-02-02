peso = float(input('Qual o seu peso? (kg)'))
altura = float(input('Qual sua altura? (m) '))
imc = (peso/(altura**2))
if imc < 18.5:
    print(f'Seu imc é {imc:.0f} você está abaixo do peso')
elif 18.5 < imc <25:
    print(f'Seu imc é {imc:.0f} você está no peso ideal')
elif 25 < imc < 30:
    print(f'Seu imc é {imc:.0f} você está sobrepeso')
elif 30 < imc < 40:
    print(f'Seu imc é {imc:.0f} você está com obesidade')
else:
    print(f'Seu imc foi {imc:.0f} você está com obesidade mórbida')
