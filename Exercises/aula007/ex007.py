from Libraries.numeric_check import isfloat
from math import ceil

print(f'[@] Envie para mim duas notas de 0 a 10:')
while True:
    grade1 = input('1: ')
    if isfloat(grade1):
        grade1 = float(grade1)
        if 10 >= grade1 >= 0:
            break
        else:
            print(f'[@] \033[1;31m{grade1} não está entre 0 e 10!\033[m')
    else:
        print(f'[@] \033[1;31m{grade1} não é um número válido!\033[m')

while True:
    grade2 = input('2: ')
    if isfloat(grade2):
        grade2 = float(grade2)
        if 10 >= grade2 >= 0:
            break
        else:
            print(f'[@] \033[1;31m{grade2} não está entre 0 e 10!\033[m')
    else:
        print(f'[@] \033[1;31m{grade2} não é um número válido!\033[m')

media = (grade1 + grade2) / 2
mediac = ceil(media*10)/10
print(f'[@] Aqui está a média: {media:.2f}')
print(f'[@] E aqui está a média arredondada: {mediac:.2f}')
