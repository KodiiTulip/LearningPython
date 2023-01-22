from Libraries.numeric_check import isfloat


categ = ['Kilômetros', 'Hectômetros', 'Dacâmetros', 'Metros', 'Decímetros', 'Centímetros', 'Milímetros']
categ_s = ['km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm']

print(f'[@] Envie para mim um valor qualquer em metros:')
while True:
    meters = input('>>> ')
    if isfloat(meters):
        meters = float(meters)
        break
    else:
        print(f'[@] \033[1;31m"{meters}" não é um valor válido!\033[m')

for i in range(0, 7):
    print(f'[@] {categ[i]}: {meters * (10**(i - 3))} {categ_s[i]}')
