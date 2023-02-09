from Libraries.numeric_check import isint

print(f'[@] Quantos valores de Fibonacci vc deseja?')
while True:
    n = input(f'>>> ')
    if isint(n):
        n = int(n)
        break
    else:
        print(f'[@] \033[1;31m"{n}" não é válido!\033[m')
f = [0, 1]
if n >= 2:
    for i in range(2, n):
        f.insert(i, f[i - 1] + f[i - 2])
    print(f'[@] aqui está:')
    print(f'[@]: ', end='')
    for o in range(len(f) - 1):
        print(f'{f[o]}', end=' - ')
    print(f'{f[len(f) - 1]}')
elif n < 2:
    print(f'[@] aqui está:')
    print(f'[@]:', end='')
    for o in range(len(f) - 1):
        print(f'{f[o]}', end=' - ')
    print(f'{f[len(f) - 1]}')
