razão = int(input('Razão: '))
pt = int(input('Primeiro termo: '))
décimo = pt + (10-1) * razão
for pa in range(pt,décimo + razão,razão):
    print(pa, end='-')
