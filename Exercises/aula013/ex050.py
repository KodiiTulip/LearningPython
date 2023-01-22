from time import sleep
from Libraries.numeric_check import isint

print(f'[@] Vou lhe pedir 6 números inteiros:')
num = []
for i in range(6):
    while True:
        num.insert(i, input(f'[{i + 1}º]: '))
        if isint(num[i]):
            num[i] = int(num[i])
            break
        else:
            print(f'[@] \033[1;31m"{num[i]}" não é válido!\033[m')
            num.pop(i)
print(f'[@] Analisando', end='')
for o in range(3):
    print(f'.', end='')
    sleep(.5)
print(f'.')
print(f'[@] Aqui todos os números pares:')
numsu = []
for r in range(6):
    if num[r] % 2 == 0:
        print(f'[@]: {num[r]}')
        sleep(.25)
        numsu.append(num[r])
numsum = sum(numsu)
print(f'[@] A soma de todos os números pares é', end='')
for o in range(3):
    print(f'.', end='')
    sleep(.5)
print(f'.')
print(f'[@]: {numsum}')
