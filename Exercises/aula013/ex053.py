from time import sleep

print(f'[@] Envie uma frase e testarei se é uma palíndromo')
frase = input(f'>>> ')
esarf = frase[::-1]
print(f'[@] Analisando', end='')
for o in range(3):
    print(f'.', end='')
    sleep(.5)
print(f'.')
print(f'[@] Aqui está o resultado:')
print(f'[@] Frase Normal: "{frase.lower()}"')
print(f'[@] Frase Invertida: "{esarf.lower()}"')
if esarf.replace(' ', '').lower() == frase.replace(' ', '').lower():
    print(f'[@] A frase inserida é um palíndromo')
else:
    print(f'[@] A frase inserida não é um palíndromo')
