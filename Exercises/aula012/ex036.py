# programa para aprovar o emprestimo bancário de uma casa
# o programa vai perguntar o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar
#
# calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado
from Libraries.numeric_check import isfloat, isint

print(f'[@] digite para mim o valor da casa, o salário do comprador e o período de pagamento:')
while True:
    vc = input(f'[@] Valor da casa\n>>> RS$')
    if isfloat(vc):
        vc = float(vc)
        if vc == 0:
            print(f'[@] Nem mesmo um pedaço de grama é gratis nesse mundo captalista.')
        elif vc < 0:
            print(f'[@] \033[1;31m"{vc}" não é válido!\033[m')
        else:
            break
    else:
        print(f'[@] \033[1;31m"{vc}" não é válido!\033[m')

while True:
    sal = input(f'[@] Salário do comprador\n>>> RS$')
    if isfloat(sal):
        sal = float(sal)
        if sal <= 0:
            print(f'[@] Perdão mas... Você tem certeza que colocou o salário correto?\n'
                  f'[@] Como você sobrevive com RS${sal:.2f} ao mês?')
        else:
            break
    else:
        print(f'[@] \033[1;31m"{sal}" não é válido!\033[m')

while True:
    praz = input(f'[@] Período de pagamento em anos\n>>> ')
    if isint(praz):
        praz = int(praz)
        if praz <= 0:
            print(f'[@] Eu presumo que você pretenda pagar algum dia.\n'
                  f'[@] Mas {praz} anos não é a resposta.')
        else:
            break
    else:
        print(f'[@] \033[1;31m"{praz}" não é válido!\033[m')

pres = vc / (praz * 12)
print(f'[@] Sua prestação mensal sem juros é RS${pres:.2f}')
if pres > sal * .3:
    print(f'[@] Infelizmente sua prestção excede 30% do seu salario (RS${sal * .3:.2f})\n'
          f'[@] Portanto o empréstimo foi negado.')
else:
    print(f'[@] Meus parabéns! O empréstimo foi aceito com sucesso!')
