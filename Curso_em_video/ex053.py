frase = str(input('Difite uma frase: ')).upper().strip()
palavras = frase.split(' ')
junto = ''.join(palavras)
inverso = ''
for letras in range (len(junto)-1, -1, -1):
    inverso += junto[letras]
if inverso == junto:
    print(f'{junto} ao contrário é {inverso} logo, é um palindromo')
else:
    print(f'{junto} ao contrario é {inverso}, logo não é um palindromo')
