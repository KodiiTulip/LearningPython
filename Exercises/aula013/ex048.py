from time import sleep

from Libraries.numeric_check import isint

print(f'[@] Irei somar todos os numeros impares múltiplos de 3 entre os números que você escolher:')
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
print(f'[@] Aqui todos os números impares múltiplos de 3:')
ks = []
if num[0] % 2 == 0:
    for k in range(num[0] + 1, num[1] + 1, 2):
        if k % 3 == 0:
            print(f'[@] {k}')
            sleep(.25)
            ks.append(k)
        else:
            sleep(0)
else:
    for k in range(num[0], num[1] + 1, 2):
        if k % 3 == 0:
            print(f'[@] {k}')
            sleep(.25)
            ks.append(k)
        else:
            sleep(0)
ksf = sum(ks)
print(f'[@] Somando todos eles', end='')
for o in range(3):
    print(f'.', end='')
    sleep(.5)
print(f'.')
print(f'[@] {ksf}')
