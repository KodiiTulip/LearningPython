from time import sleep
from Libraries.numeric_check import isfloat, isint

while True:
    num = []
    print(f'[@] Digite para mim dois números:')
    for i in range(0, 2):
        while True:
            num.insert(i, input(f'[{i + 1}]: >>> '))
            if isfloat(num[i]):
                num[i] = float(num[i])
                break
            else:
                print(f'[@] \033[1;31m"{num[i]}" não é válido!\033[m')
        sleep(.2)
    while True:
        opc = ['Somar', 'Multiplicar', 'Qual o maior', 'Novos números', 'Sair']
        print(f'[@] Escolha uma das opções:')
        for o in range(0, len(opc)):
            print(f'[{o+1}]: {opc[o]}')
            sleep(.3)
        while True:
            opcao = input(f'>>> ')
            if isint(opcao):
                opcao = int(opcao)
                if 6 > opcao > 0:
                    break
                else:
                    print(f'[@] \033[1;31m"{opcao}" não é válido!\033[m')
            else:
                print(f'[@] \033[1;31m"{opcao}" não é válido!\033[m')
        if opcao == 5:
            break
        elif opcao == 1:
            print(f'\n[@] {num[0]} + {num[1]} = {num[0] + num[1]}\n')

        elif opcao == 2:
            print(f'\n[@] {num[0]} * {num[1]} = {num[0] * num[1]}\n')

        elif opcao == 3:
            print(f'\n[@] o maior número é: {max(num)}\n')
            
        elif opcao == 4:
            break
    if opcao == 5:
        break
