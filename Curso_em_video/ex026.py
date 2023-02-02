frase = str(input('Digite uma frase: '))
frase = frase.upper()
print(f'A frase possui {(frase.count("A"))} letras A\nPrimeira letra A está em {(frase.find("A"))}\nE a última está em {(frase.rfind("A"))}')
