# programa ler 3 números e mostre eles em ordem decrescente
from Libraries.numeric_check import isfloat

num = ['', '', '']
print(f'[@] digite para mim 3 números diferentes:')
for i in range(0, 3):
    while True:
        num[i] = input(f'[@] {i + 1}º número: ')
        if isfloat(num[i]):
            num[i] = float(num[i])
            break
        else:
            print(f'[@] \033[1;31m"{num[i]}" não é válido!\033[m')
num.sort(reverse=True)
print(f'[#] Aqui os números em ordem decrescente:')
for o in range(0, len(num)):
    print(f'[#] {o + 1}º: {num[o]}')
