from time import sleep
from Libraries.numeric_check import isint

print(f'[@] Vou verificar se o seu número é primo:')
while True:
    num = input(f'>>> ')
    if isint(num):
        num = int(num)
        break
    else:
        print(f'[@] \033[1;31m"{num}" não é válido!\033[m')
mul = 0
for i in range(2, num - 1):
    if num % i == 0:
        print(f'[@] Multiplo de {i}')
        mul += 1
        sleep(.5)

if mul == 0:
    print(f'[@] O número "{num}" é um número primo.')
else:
    print(f'[@] O número "{num}" não é um número primo, e possui {mul} divisores')
