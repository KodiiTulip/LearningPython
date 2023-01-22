# programa ler um ano e afirma se ele é um ano bissexto
from Libraries.numeric_check import isint

print(f'[@] Digite um ano qualquer')
while True:
    ano = input(f'>>> ')
    if isint(ano):
        ano = int(ano)
        break
    else:
        print(f'[@] \033[1;31m"{ano}" não é válido!\033[m')
if (ano % 4) == 0:
    print(f'[#] {ano} é um ano bissexto.')
else:
    print(f'[#] {ano} não é um ano bissexto.')
