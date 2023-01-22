# programa le dois números inteiros e campara eles, mostrando se o maior número eh o primeiro ou o segundo ou nenhum
from Libraries.numeric_check import isint

print(f'[@] Digite dois números inteiros.')
n = ['', '']
for i in range(0, 2):
    while True:
        n[i] = input(f'[{i + 1}º]: ')
        if isint(n[i]):
            n[i] = int(n[i])
            break
        else:
            print(f'[@] \033[1;31m"{n[i]}" não é válido!\033[m')

if n[0] > n[1]:
    print(f'[@] O primeiro valor é maior')
elif n[0] < n[1]:
    print(f'[@] O segundo valor é maior')
if n[0] == n[1]:
    print(f'[@] Ambos valores são iguais')
