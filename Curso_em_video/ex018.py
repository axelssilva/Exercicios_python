from math import sin, cos, tan, radians
a = float(input('Digite um ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print(f'O ângulo {a} possuí\nseno: {s:.2f}\nCosseno {c:.2f}\nTangente{t:.2f}')
