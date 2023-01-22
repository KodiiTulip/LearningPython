from Libraries.numeric_check import isfloat, isint

print(f'[@] Qual o preço base do produto?')
while True:
    price = input(f'>>> RS$')
    if isfloat(price):
        price = float(price)
        break
    else:
        print(f'[@] \033[1;31m"{price}" não é válido!\033[m')

opc = ['À VISTA(DINHEIRO/CHEQUE)', 'À VISTA(CARTÃO)', 'PARCELADO(CARTÃO)']
print(f'[@] Qual a condição de pagamento?')
for i in range(0, 3):
    print(f'[{i + 1}]: {opc[i]}')
while True:
    ch = input(f'>>> ')
    if isint(ch):
        ch = int(ch)
        if ch in range(1, 4):
            break
        else:
            print(f'[@] \033[1;31m"{ch}" não é válido!\033[m')
    else:
        print(f'[@] \033[1;31m"{ch}" não é válido!\033[m')

if ch == 3:
    while True:
        print(f'[@] quantas parcelas serão?')
        par = input(f'>>> ')
        if isint(par):
            par = int(par)
            if par >= 3:
                juros = price * .2 * par
                montante = price + juros
                print(f'[@] Irá pagar RS${montante:.2f} após parcelamento, com RS${juros:.2f} de juros\n'
                      f'[@] Por tanto será RS${montante/par:.2f} ao mês')
                break
            elif 3 > par > 1:
                print(f'[@] irá pagar RS${price / par:.2f} ao mes')
                break
            else:
                print(f'[@] \033[1;31m"{par}" não é válido!\033[m')
        else:
            print(f'[@] \033[1;31m"{par}" não é válido!\033[m')
elif ch == 2:
    pricef2 = price - (price * .05)
    print(f'[@] Irá pagar RS${pricef2:.2f}')
elif ch == 1:
    pricef1 = price - (price * .1)
    print(f'[@] Irá pagar RS${pricef1:.2f}')
