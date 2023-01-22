
print(f'[@] digite uma frase:')
frase = input(f'>>> ')
frase = frase.strip()
print(f'\n[@]: {frase}')

print(f'[@]: Quantas vezes aparecem a letra A?')
frase1 = frase.lower()
a = frase1.count('a')
if a == 1:
    print(f'[#]: {a} vez')
else:
    print(f'[#]: {a} vezes')
print(f'[@]: Em qual posição a letra A aparece pela primeira vez?')
ap = frase1.find('a') + 1
if a > 0:
    print(f'[#]: A primeira posição da letra A é {ap}º posição')
else:
    print(f'[#]: A letra A não aparece na frase')
print(f'[@]: Em qual posição a letra A aparece pela última vez?')
apu = frase1.rfind('a') + 1
if a > 0:
    print(f'[#]: A última posição da letra A é {apu}º posição')
else:
    print(f'[#]: A letra A não aparece na frase')
