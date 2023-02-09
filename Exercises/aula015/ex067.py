from Libraries.numeric_check import isint

while True:
    print(f'[@] Envie para mim um número para visualizar sua tabuada.\n'
          f'(números negativos finalizam o programa)')
    while True:
        n = (input('>> '))
        if isint(n):
            n = int(n)
            break
        else:
            print(f'[@] \033[1;31m"{n}" não é válido\033[m')
    if n < 0:
        print(f'[@] Finalizando programa...')
        break
    print('==' + '-' * 16 + '==')
    for i in range(0, 11):
        print(f"{f'{n: >2} * {i: <2} = {n * i: <3}': ^21}")
    print('==' + '-' * 16 + '==')
