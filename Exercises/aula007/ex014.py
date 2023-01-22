from Libraries.numeric_check import isfloat

print(f'[@] Envie uma temperatura em ºC e eu a converterei em ºF.')
while True:
    tempc = input(f'ºC')
    if isfloat(tempc):
        tempc = float(tempc)
        break
    else:
        print(f'[@] \033[1;31m"{tempc}" não é válido!\033[m')

tempf = ((9/5) * tempc) + 32
print(f'[@] A temperatura {tempc} ºC equivale a {tempf} ºF')
