from Libraries.numeric_check import isfloat


# US$1.00 == RS$5.34
tax = 5.34
print(f'[@] Quanto dinheiro você tem acumulado?')
while True:
    money = input('>> RS$')
    if isfloat(money):
        money = float(money)
        break
    else:
        print(f'[@] \033[1;31m"{money}" não é valido!\033[m')

dollar = money / tax
print(f'[@] Você tem, em dolares: US${dollar: .2f}')
