from Libraries.numeric_check import isfloat

n1 = (input('[@] Digite um número: '))

n2 = (input('[@] Digite um segundo número: '))


if isfloat(n1) and not isfloat(n2):
    print(f'[@] \033[1;31m"{n2}" não é um valor numérico.\033[m')
    exit()
else:
    if not isfloat(n1) and isfloat(n2):
        print(f'[@] \033[1;31m"{n1}" não é um valor numérico.\033[m')
        exit()
    else:
        if isfloat(n1) and isfloat(n2):
            n1 = float(n1)
            n2 = float(n2)
            if n1.is_integer() and n2.is_integer():
                n1 = int(n1)
                n2 = int(n2)
            s = n1 + n2
            print(f'[@] A soma entre {n1} e {n2} vale {s}')

        else:
            print(f'[@] "{n1}" e "{n2}" não são numéricos.')
