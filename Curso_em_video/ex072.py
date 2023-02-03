num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número de 0 a 20: '))
entrada = list(range(0,21))
while n not in entrada:
   n = int(input('Comando inválido. Digite um número entre 0 e 20: '))
print(f'{n} por extenso é {num[n]}')

