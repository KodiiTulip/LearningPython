from time import sleep
from Libraries.numeric_check import isint


gender = []
age = []
name = []
oldestm = 0
oldestmname = ''
youngf = 0
for i in range(4):
    print(f'-----[{i + 1}º Pessoa]-----')
    print(f'[@] Qual o seu nome?')
    name.insert(i, input(f'>>> '))
    print(f'[@] Qual a sua idade?')
    while True:
        age.insert(i, input(f'>>> '))
        if isint(age[i]):
            age[i] = int(age[i])
            break
        else:
            print(f'[@] \033[1;31m"{age[i]}" não é válido!\033[m')
            age.pop(i)
    print(f'[@] Qual seu gênero?\n'
          f'[1]: Masculino\n'
          f'[2]: Feminino\n'
          f'[3]: Outro')
    while True:
        gender.insert(i, input(f'>>> '))
        if isint(gender[i]):
            gender[i] = int(gender[i])
            if 1 <= gender[i] <= 3:
                break
            else:
                print(f'[@] "{gender[i]}" não está entre as opções!')
                gender.pop(i)
        else:
            print(f'[@] \033[1;31m"{gender[i]}" não é válido!\033[m')
            gender.pop(i)
    if i == 0 and gender[i] == 1:
        oldestm = age[i]
        oldestmname = name[i]
    if gender[i] == 1 and age[i] > oldestm:
        oldestm = age[i]
        oldestmname = name[i]
    if gender[i] == 2 and age[i] < 20:
        youngf += 1

mediaage = sum(age) / len(age)
print(f'[@] Analisando', end='')
for o in range(3):
    print(f'.', end='')
    sleep(.5)
print(f'.')
print(f'[@] Aqui está o resultado:')
print(f'[@] A média de idade do grupo é: {mediaage} anos\n'
      f'[@] O homem mais velho é {oldestmname} com {oldestm} anos\n'
      f'[@] Existem {youngf} mulheres com menos de 20 anos')
