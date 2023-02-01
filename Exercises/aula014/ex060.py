from Libraries.numeric_check import isfloat

print(f'[@] Digite para mim um número:')
while True:
    num = input(f'>>> ')
    if isfloat(num):
        num = int(num)
        break
    else:
        print(f'[@] \033[1;31m"{num}" não é válido!\033[m')
fat = 1
for i in range(num, 0, -1):
    fat = fat * i
print(f'[@] Valor final: {fat}')
