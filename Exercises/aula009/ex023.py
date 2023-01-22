from Libraries.numeric_check import isint

# programa que leia um número de 0 a 9999 e mostrecada um dos dígitos separados
chan = ['Unidade', 'Dezena', 'Centena', 'Uni Milhar']
print(f'[@] digite um número inteiro entre 0 e 9999')
while True:
    n = input(f'>>> ')
    if isint(n):
        break
    else:
        print(f'[@] \033[1;31m"{n}" não é válido!\033[m')

for i in range(0, len(n)):
    print(f'[@] {chan[i]}: {n[(len(n) - 1) - i]}')
