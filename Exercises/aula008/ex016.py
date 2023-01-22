from Libraries.numeric_check import isfloat
from math import trunc

# crie um programa que leia um número real qualquer entregue pelo usuário e mostre a porção inteira dese número

print(f'[@] Insira um número real qualquer:')
while True:
    n = input(f'>>> ')
    if isfloat(n):
        n = float(n)
        nt = trunc(n)
        break
    else:
        print(f'[@] \033[1;31m"{n}" não é válido!\033[m')

print(f'[@] O número {n} possui a sua parte inteira equivalente a {nt}.')
