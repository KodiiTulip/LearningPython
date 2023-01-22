from Libraries.numeric_check import isint

print(f'[@] Digite o ano atual:')
while True:
    ano = input(f'>>> ')
    if isint(ano):
        ano = int(ano)
        break
    else:
        print(f'[@] \033[1;31m{ano} não é válido!\033[m')

print(f'[@] Digite o ano de nascimento do candidato:')
while True:
    birth = input(f'>>> ')
    if isint(birth):
        birth = int(birth)
        if birth > ano:
            print(f'[@] Algo me parece incorreto...\n[@] O ano atual é {ano}, mas o candidato nascem em {birth}?')
        else:
            break
    else:
        print(f'[@] \033[1;31m{birth} não é válido!\033[m')
print(f'[@] {ano - birth} aninhos\n[@] Vamos ver em qual categoria elu irá!')
if ano - birth <= 9:
    print(f'[@] Elu participará da categoria \033[1mMIRIN\033[m')
elif 9 < ano - birth <= 14:
    print(f'[@] Elu participará da categoria \033[1mIFANTIL\033[m')
elif 14 < ano - birth <= 19:
    print(f'[@] Elu participará da categoria \033[1mJUNIOR\033[m')
elif 19 < ano - birth <= 20:
    print(f'[@] Elu participará da categoria \033[1mSÊNIOR\033[m')
elif 20 < ano - birth:
    print(f'[@] Elu participará da categoria \033[1mMASTER\033[m')
