palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nA palavra {p} tem as seguintes vogais ', end= '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')
