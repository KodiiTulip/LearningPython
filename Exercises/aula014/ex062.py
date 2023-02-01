from time import sleep
from Libraries.numeric_check import isint

while True:
    print(f'\n\n[@] No primeiro número coloque o primeiro termo de uma PA.\n'
          f'[@] No segundo,  coloque a razão dessa mesma PA.\n'
          f'[@] No terceiro, coloque quantos termos deseja mostrar (coloque 0 para finalizar o programa).')
    num = []
    for i in range(3):
        while True:
            num.insert(i, input(f'[{i + 1}º]: '))
            if isint(num[i]):
                num[i] = int(num[i])
                break
            else:
                print(f'[@] \033[1;31m"{num[i]}" não é válido!\033[m')
                num.pop(i)
    if num[2] == 0:
        break
    print(f'[@] Aqui os {num[2]} primeiros termos dessa PA:')
    n = 1
    while n != (num[2] + 1):
        numberfinal = num[0] + (n - 1) * num[1]
        print(f'[{n:0>2}º]: {numberfinal}')
        sleep(.5)
        n += 1
