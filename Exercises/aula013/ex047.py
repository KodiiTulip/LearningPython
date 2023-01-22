from time import sleep

from Libraries.numeric_check import isint

print(f'[@] Irei digitar agora todos os numeros pares entre os números que você escolher:')
while True:
    num = []
    for i in range(2):
        while True:
            num.insert(i, input(f'[{i + 1}º]: '))
            if isint(num[i]):
                num[i] = int(num[i])
                break
            else:
                print(f'[@] \033[1;31m"{num[i]}" não é válido!\033[m')
                num.pop(i)
    if num[0] < num[1]:
        break
    else:
        print(f'[@] Porfavor, coloque o primeiro número sendo menor do que o segundo.')


print(f'[@] Analisando', end='')
for o in range(5):
    print(f'.', end='')
    sleep(.5)
print(f'.')

if num[0] % 2 == 0:
    for k in range(num[0], num[1] + 1, 2):
        print(f'[@] {k}')
        sleep(.25)
else:
    for k in range(num[0] + 1, num[1] + 1, 2):
        print(f'[@] {k}')
        sleep(.25)
