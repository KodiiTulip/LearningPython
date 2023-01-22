# leia um número inteiro qualquer e mostre se ele é par ou impar
from Libraries.numeric_check import isint

par = ['0', '2', '4', '6', '8']
impar = ['1', '3', '5', '7', '9']

print(f'[@] Digite um número inteiro qualquer:')
while True:
    n = input(f'>>> ')
    if isint(n):
        n = int(n)
        break
    else:
        print(f'[@] \033[1;31m"{n}" não é válido!\033[m')
if (n % 2) == 0:
    print(f'[@] O número {n} é par!')
else:
    print(f'[@] O número {n} é impar!')
