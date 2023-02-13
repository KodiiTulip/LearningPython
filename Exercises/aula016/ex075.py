print(f'[@] Digite 4 números inteiros:')
num = (int(input(f'[1º] >>> ')),
       int(input(f'[2º] >>> ')),
       int(input(f'[3º] >>> ')),
       int(input(f'[4º] >>> ')))
print(f'[@] Os números foram: {num}\n'
      f'[@] O número 9 apareceu: {num.count(9)}\n'
      f'[@] O número 3 está na posição: {num.index(3) + 1}\n'
      f'[@] Os números pares foram:\n'
      f'[@] ', end='')
for i in range(len(num)):
    if num[i] % 2 == 0:
        print(num[i], end=' ')
