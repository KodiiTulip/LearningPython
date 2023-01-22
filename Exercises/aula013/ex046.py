import time

from Libraries.numeric_check import isint

print(f'[@] Quantos segundos para o timer?')
while True:
    sec = input(f'>>> ')
    if isint(sec):
        sec = int(sec)
        break
    else:
        print(f'[@] \033[1;31m"{sec}" não é válido!\033[m')

for i in range(sec, -1, -1):
    print(f'[@] {i}!')
    time.sleep(1)

print(f'[@] O timer de {sec} segundos terminou.')
