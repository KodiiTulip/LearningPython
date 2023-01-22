from time import sleep
from Libraries.numeric_check import isint

print(f'[@] Qual o ano atual?')
while True:
    ano = input(f'>>> ')
    if isint(ano):
        ano = int(ano)
        break
    else:
        print(f'[@] \033[1;31m"{ano}" não é válido!\033[m')

print(f'[@] Digite o ano de nascimento de sete pessoas:')
num = []
for i in range(7):
    while True:
        num.insert(i, input(f'[{i + 1}º]: '))
        if isint(num[i]):
            num[i] = int(num[i])
            break
        else:
            print(f'[@] \033[1;31m"{num[i]}" não é válido!\033[m')
            num.pop(i)
minors = 0
majors = 0
wrong = 0
for o in range(7):
    if ano - num[o] < 18:
        minors += 1
    elif ano - num[o] >= 18:
        majors += 1
    if ano - num[o] < 0:
        wrong += 1

print(f'[@] Analisando', end='')
for o in range(3):
    print(f'.', end='')
    sleep(.5)
print(f'.')
print(f'[@] Aqui está o resultado:')
print(f'[@] Temos aqui {minors} menores de idade\n'
      f'[@] Temos aqui {majors} maiores de idade\n'
      f'[@] Temos aqui {wrong} que tivera idade negativa...')
