from time import sleep
from Libraries.numeric_check import isint

print(f'[@] No primeiro número coloque o primeiro termo de uma PA.\n'
      f'[@] No segundo,  coloque a razão dessa mesma PA.')
num = []
for i in range(2):
    while True:
        num.insert(i, input(f'[{i + 1}º]: '))
        if isint(num[i]):
            num[i] = int(num[i])
            break
        else:
            print(f'[@] \033[1;31m"{num[i]}" não é válido!\033[m')
            num.pop(i)

print(f'[@] Aqui os 10 primeiros termos desa PA:')
n = 1
while n != 11:
    numberfinal = num[0] + (n - 1) * num[1]
    print(f'[{n:0>2}º]: {numberfinal}')
    sleep(.5)
    n += 1
