from Libraries.numeric_check import isfloat

print(f'[@] Digite um número:')
value = False
num = []
while True:
    num.append(input(f'>>> '))
    if isfloat(num[len(num) - 1]):
        num[len(num) - 1] = float(num[len(num) - 1])
        print(f'[@] Você deseja adicionar mais um número?')
        valuei = input('[Y/N] >>> ')
        if valuei in 'nN':
            value = True
            break
    else:
        print(f'[@] \033[1;31m"{num[len(num) - 1]}" não é válido!\033[m')
if value:
    print(f'[@] Okay.\n'
          f'[@] Aqui está quantos números você digitou:\n'
          f'[@] {len(num)} números.\n'
          f'[@] Somando todos eles fica: {sum(num)}\n'
          f'[@] A média entre eles fica: {sum(num)/len(num)}\n'
          f'[@] O maior valor foi: {max(num)}\n'
          f'[@] O menor valor foi: {min(num)}')
