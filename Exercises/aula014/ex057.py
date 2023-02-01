from Libraries.numeric_check import isint

print(f'[@] Qual seu gênero?\n'
      f'[1]: Masculino\n'
      f'[2]: Feminino\n'
      f'[3]: Não-Binárie\n'
      f'[4]: Outro')
while True:
    gender = input(f'>>> ')
    if isint(gender):
        gender = int(gender)
        if 1 <= gender <= 4:
            break
        else:
            print(f'[@] "{gender}" não está entre as opções!')
    else:
        print(f'[@] \033[1;31m"{gender}" não é válido!\033[m')
