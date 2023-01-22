from Libraries.numeric_check import isfloat
while True:
    n = input('[@] Digite um número: ')
    if isfloat(n):
        n = float(n)
        su = n + 1
        an = n - 1
        print(f'[@] Analisando...\nAntecessor: {an: .1f}\nSucessor: {su: .1f}')
        exit()
    else:
        print(f'[@] Analisando...\n"{n}" não é um número válido!\n')
