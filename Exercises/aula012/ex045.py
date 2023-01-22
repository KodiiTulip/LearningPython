from Libraries.numeric_check import isint
import random

print(f'[@] pedra, papel ou tessoura! VAI!\n')
opc = ['Pedra', 'Papel', 'Tesoura']
for i in range(0, 3):
    print(f'[{i + 1}]: {opc[i]}')
print(f'')
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

ch_pc = random.randint(1, 3)
if ch == ch_pc:
    print(f'[@] Um empate! Voce escolheu {opc[ch - 1]} e eu escolhi {opc[ch_pc - 1]}')
elif ch == 1 and ch_pc == 2 or ch == 2 and ch_pc == 3 or ch == 3 and ch_pc == 1:
    print(f'[@] EU GANHEI! Voce escolheu {opc[ch - 1]} e eu escolhi {opc[ch_pc - 1]}')
elif ch == 1 and ch_pc == 3 or ch == 2 and ch_pc == 1 or ch == 3 and ch_pc == 2:
    print(f'[@] VOCÊ GANHOU! Voce escolheu {opc[ch - 1]} e eu escolhi {opc[ch_pc - 1]}')
