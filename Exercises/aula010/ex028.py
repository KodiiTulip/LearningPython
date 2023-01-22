# programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.
import random

from Libraries.numeric_check import isint

opc = []

print(f'[@] Eu estou pensando em um número...')
print(f'[@] Você consegue adivinhar? Aqui estão algumas opçõe para te ajudar!')

rnum1 = random.randint(0, 2)
rnum2 = random.randint(0, 5)
while True:
    rnum3 = random.randint(0, 5)
    if rnum3 != rnum2:
        break
while True:
    rnum4 = random.randint(0, 5)
    if rnum4 != rnum3 and rnum4 != rnum2:
        break

opc.insert(0, rnum2)
opc.insert(1, rnum3)
opc.insert(2, rnum4)

print(f'[@]   {opc[0]: <3}{opc[1]: ^5}{opc[2]: >3}')

while True:
    answer = input(f'>>> ')
    if isint(answer):
        answer = int(answer)
        if 6 > answer > -1:
            break
        else:
            print(f'[@] \033[1;31m"{answer}" não está entre as opções.\033[m')
    else:
        print(f'[@] \033[1;31m"{answer}" não é válido!\033[m')
if answer == opc[rnum1]:
    print(f'[@] PARBÉNS!!! O número que eu estava pensando era {answer}!!')
else:
    print(f'[@] Desculpe anjinho mas {answer} não era o número escolhido, mas sim o {opc[rnum1]}.')
