from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjascente: '))
hipo = hypot(ca,co)
print(f'A hipotenusa é igual a {hipo:.3f}')
