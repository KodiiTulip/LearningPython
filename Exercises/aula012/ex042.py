# prgrama ler o comprimeto de tres retas e diz ao usuario se elas podem ou não formar um trângulo
from Libraries.numeric_check import isfloat

num = ['', '', '']
print(f'[@] digite para mim 3 comprimentos de reta diferentes:')
for i in range(0, 3):
    while True:
        num[i] = input(f'[@] {i + 1}º número: ')
        if isfloat(num[i]):
            num[i] = float(num[i])
            break
        else:
            print(f'[@] \033[1;31m"{num[i]}" não é válido!\033[m')
num.sort(reverse=True)

minnum = [num[1] - num[2], num[0] - num[2], num[0] - num[1]]
maxnum = [num[1] + num[2], num[0] + num[2], num[0] + num[1]]

if minnum[0] < num[0] < maxnum[0] and minnum[1] < num[1] < maxnum[1] and minnum[2] < num[2] < maxnum[2]:
    print(f'[@] É possivel fazer um triangulo com esses valores?\n[#] Sim.')
    tri = True
else:
    print(f'[@] É possivel fazer um triangulo com esses valores?\n[#] Não.')
    tri = False

side = [num[0] == num[1], num[0] == num[2], num[1] == num[2]]
if tri:
    if num[0] == num[1] == num[2]:
        print(f'[#] É um trinagulo equilátero')
    elif side[0] or side[1] or side[2]:
        print(f'[#] É um trinagulo isóceles')
    else:
        print(f'[#] É um trinagulo escaleno')
