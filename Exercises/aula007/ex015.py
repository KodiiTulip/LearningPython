from Libraries.numeric_check import isfloat, isint

print(f'[@] Cálculo de aluguel de carro')
while True:
    days = input(f'[@] Por quantos dias o carro foi alugado?\n>> ')
    if isint(days):
        days = int(days)
        break
    else:
        print(f'[@] \033[1;31m"{days}" não é válido!\033[m')

while True:
    km = input(f'[@] Quantos quilômetros foram rodados?\n>> ')
    if isfloat(km):
        km = float(km)
        break
    else:
        print(f'[@] \033[1;31m"{km}" não é válido!\033[m')

rent = (60 * days) + (.15 * km)
print(f'[@] O total a pagar do aluguel é: RS${rent:.2f}')
