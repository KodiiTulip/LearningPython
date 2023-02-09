import random

from Libraries.numeric_check import isint

print(f'=='+'-'*10+'==')
print(f'{f"PAR OU IMPAR": ^14}')
print(f'=='+'-'*10+'==')

while True:
    plvalue = 0
    pc = random.randint(0, 10)
    print('[@] Digite um valor:')
    while True:
        pl = input('>>> ')
        if isint(pl):
            pl = int(pl)
            if pl > 10:
                print(f'[@] O valor máximo é 10.')
            else:
                break
        else:
            print(f'[@] \033[1;31m"{pl}" não é válido\033[m')
    print(f'[@] Par ou Impar?')
    while True:
        pli = input('>>> ')
        if pli in ['Par', 'par', 'PAR']:
            plvalue = 0
            break
        elif pli in ['Impar', 'impar', 'IMPAR']:
            plvalue = 1
            break
        else:
            print(f'[@] \033[1;31m"{pli}" não é válido\033[m')
    print(f'{plvalue}'
          f'==' + '-' * 10 + '==\n'
          f'[@] Computador: {pc}\n'
          f'[@] Player: {pl}')
    if (pl + pc) % 2 == 0:
        print(f'[@] Deu Par.')
    elif (pl + pc) % 2 != 0:
        print(f'[@] Deu Impar.')
    if plvalue == 1:
        if (pl + pc) % 2 != 0:
            print(f'[@] Você venceu!!\n'
                  f'[@] Vamos de novo!!\n'
                  f'==' + '-' * 10 + '==')
        elif (pl + pc) % 2 == 0:
            print(f'[@] Você perdeu.\n'
                  f'[@] Game over.\n'
                  f'==' + '-' * 10 + '==')
            break
    elif plvalue == 0:
        if (pl + pc) % 2 == 0:
            print(f'[@] Você venceu!!\n'
                  f'[@] Vamos de novo!!\n'
                  f'==' + '-' * 10 + '==')
        elif (pl + pc) % 2 != 0:
            print(f'[@] Você perdeu.\n'
                  f'[@] Game over.\n'
                  f'==' + '-' * 10 + '==')
            break
