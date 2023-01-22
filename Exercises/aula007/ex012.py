from Libraries.numeric_check import isfloat


print(f'[@] Envie para mim o preço original do objeto,')
print(f'[@] e eu lhe enviarei o preço com o desconto desejado!')

while True:
    price = input('>> RS$')
    if isfloat(price):
        price = float(price)
        break
    else:
        print(f'[@] \033[1;31m"{price}" não é válido!\033[m')

while True:
    descon = input('>> Desconto em %')
    if isfloat(descon):
        descon = float(descon)
        break
    else:
        print(f'[@] \033[1;31m"{descon}" não é válido!\033[m')

descon_f = descon * 10**-2
new_price = price - (price * descon_f)

print(f'[@] Novo preço com {descon}% de desconto: RS${new_price: .2f}')
