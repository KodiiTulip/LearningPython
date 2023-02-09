from Libraries.numeric_check import isfloat

print(f'[@] Estou pensanndo em um número...\n'
      f'[@] Digite ele para mim.')
value = False
num = []
while True:
    num.append(input(f'>>> '))
    if isfloat(num[len(num) - 1]):
        num[len(num) - 1] = float(num[len(num) - 1])
        if num[len(num) - 1] == 999:
            value = True
            break
        else:
            print(f'[@] Hmmm...\n'
                  f'[@] Esse não é meu número, tente de novo.')
    else:
        print(f'[@] \033[1;31m"{num[len(num) - 1]}" não é válido!\033[m')
if value:
    print(f'[@] Meus parabéns!!!\n'
          f'[@] Aqui está quantos números você digitou antes de acertar:\n'
          f'[@] {len(num) - 1} números!\n'
          f'[@] Somando todos eles fica: {sum(num) - 999}')
