from time import sleep
from Libraries.numeric_check import isint

print(f'[@] Digite o peso de 5 pessoas:')
num = []
for i in range(5):
    while True:
        num.insert(i, input(f'[{i + 1}º]: '))
        if isint(num[i]):
            num[i] = int(num[i])
            if num[i] > 0:
                break
            else:
                print(f'[@] \033[1;31m"{num[i]}" não é válido!\033[m')
                num.pop(i)
        else:
            print(f'[@] \033[1;31m"{num[i]}" não é válido!\033[m')
            num.pop(i)
num.sort()
print(f'[@] Analisando', end='')
for o in range(3):
    print(f'.', end='')
    sleep(.5)
print(f'.')
print(f'[@] Aqui está o resultado:')
print(f'[@] Maior peso: {num[len(num)-1]}\n'
      f'[@] Menor peso: {num[0]}')
