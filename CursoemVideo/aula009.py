# fatiamento
frase = 'Curso em Vídeo Python'
print(frase[:21])
print(frase[9::2])
# analise
leng = len(frase)
print(leng)

o = frase.count('o')
print(o)

quantas = frase.find('deo')
print(f'[@] "deo" começa na posição {quantas}')
cur = frase.find('Android')
print(f'{cur}')

if 'Curso' in frase:
    print(f'True')
else:
    print(f'False')

# transformação
frase2 = frase.replace('Python', 'Android')
print(frase2)

if frase.isupper():
    frase3 = frase.lower()
    print(frase3)
else:
    frase3 = frase.upper()
    print(frase3)
if frase.istitle():
    frase3 = frase.capitalize()
    print(frase3)
else:
    frase3 = frase.title()
    print(frase3)
frase4 = '   Aprenda Python  '
print(frase4)
frase4 = frase4.strip()
print(frase4)


# divisao
frase5 = frase.split()
for i in range(0, len(frase5)):
    print(f'{frase5[i]}')

frase6 = '-'.join(frase5)
print(frase6)
