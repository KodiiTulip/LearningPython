from Libraries.numeric_check import isfloat


print(f'[@] Envie para mim o salário original do funcionário,')
print(f'[@] e eu lhe enviarei o novo salário com o aumento desejado!')

while True:
    sal = input('>> RS$')
    if isfloat(sal):
        sal = float(sal)
        break
    else:
        print(f'[@] \033[1;31m"{sal}" não é válido!\033[m')

while True:
    aumen = input('>> Aumento em %')
    if isfloat(aumen):
        aumen = float(aumen)
        break
    else:
        print(f'[@] \033[1;31m"{aumen}" não é válido!\033[m')

aumen_f = (aumen * 10**-2) + 1
new_sal = sal * aumen_f
print(f'[@] Novo salário com {aumen}% de aumento: RS${new_sal: .2f}')
