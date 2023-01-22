# programa pergunta por um número inteiro qualquer e pede ao usuário escolher a base de conversão
from Libraries.numeric_check import isint

print(f'[@] Escreva um número inteiro qualquer:')
while True:
    n = input(f'>>> ')
    if isint(n):
        n = int(n)
        break
    else:
        print(f'[@] \033[1;31m"{n}" não é válido!\033[m')

print(f"{f'[1] Binário': <12}{f'[2] Octal': ^14}{f'[3] Hexadecimal': >12}")
while True:
    ch = input(f'>>> ')
    if ch in '1 2 3' and isint(ch):
        ch = int(ch)
        break
    else:
        print(f'[@] \033[1;31m"{ch}" não é uma das opções!\033[m')

if ch == 1:
    print(f'[@] oO número {n} em Binário é: {bin(n)}')
elif ch == 2:
    print(f'[@] oO número {n} em Octal é: {oct(n)}')
elif ch == 3:
    print(f'[@] oO número {n} em Hexadecimal é: {hex(n)}')
