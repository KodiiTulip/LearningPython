# programa le o ano de nascimento de um jovem e informa de acordo com sua idade
# se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar
# se já passou do tempo do alistamento
# programa mostra o tempo que falta ou que passou do prazo
from Libraries.numeric_check import isint

print(f'[@] Qual o ano atual?')
while True:
    ano = input(f'>>> ')
    if isint(ano):
        ano = int(ano)
        break
    else:
        print(f'[@] \033[1;31m"{ano}" não é válido!\033[m')

print(f'[@] Ok! Qual seu ano de nascimento?')
while True:
    birth = input(f'>>> ')
    if isint(birth):
        birth = int(birth)
        if birth > ano:
            print(f'[@] \033[1;31m"{birth}" não é válido!\n'
                  f'\033[m[@] \033[1;31mNão tem como você ter vindo do futuro.\033[m')
        else:
            break
    else:
        print(f'[@] \033[1;31m"{birth}" não é válido!\033[m')

if ano - birth < 18:
    print(f'[@] Você ainda irá se alistar.\n[@] Faltam aproximados {18 - (ano - birth)} anos.')
elif ano - birth == 18:
    print(f'[@] Você deve se alistar esse ano.')
elif ano - birth > 18:
    print(f'[@] Você passou do tempo de se alistar.\n[@] Passaram-se aproximados {(ano - birth) - 18} anos.')
