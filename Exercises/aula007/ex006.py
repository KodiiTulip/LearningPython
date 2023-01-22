from Libraries.numeric_check import isfloat
while True:
    n = input('[@] Digite um número: ')
    if isfloat(n):
        n = float(n)
        do = n * 2
        tr = n * 3
        rq = n ** (1/2)
        print(f'[@] Analisando...\nDobro: {do: .1f}\nTriplo: {tr: .1f}\nRaiz Quadrada: {rq}')
        exit()
    else:
        print(f'[@] Analisando...\n[@] \033[1;31m"{n}" não é um número válido!\033[m')
