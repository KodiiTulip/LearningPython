# programa pergunta o salário de um funcionario e calcule o valor do aumento
# para salários superiores a 1250 calcule um aumento de 10%
# para os inferiores, um aumento de 15%.
from Libraries.numeric_check import isfloat

print(f'[@] digite o salário do funcionário:')
while True:
    sal = input(f'[@] >>> RS$')
    if isfloat(sal):
        sal = float(sal)
        break
    else:
        print(f'[@] \033[1;31m"{sal}" não é válido!\033[m')
if sal > 1250:
    salf = sal * 1.10
    print(f'[@] O salário final será: RS${salf:.2f}')
elif sal <= 1250:
    salf = sal * 1.15
    print(f'[@] O salário final será: RS${salf:.2f}')
