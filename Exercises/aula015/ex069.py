from time import sleep
from Libraries.numeric_check import isint

i = 0
people = []
while True:
    print(f'-----[{i + 1}º Pessoa]-----')
    print(f'[@] Qual o seu nome?')
    name = input(f'>>> ')
    print(f'[@] Qual a sua idade?')
    while True:  # price
        age = input(f'>>> ')
        if isint(age):
            age = int(age)
            break
        else:
            print(f'[@] \033[1;31m"{age}" não é válido!\033[m')
    print(f'[@] Qual seu gênero?\n'
          f'[1]: Masculino\n'
          f'[2]: Feminino\n'
          f'[3]: Outro')
    while True:  # gender
        gender = input(f'>>> ')
        if isint(gender):
            gender = int(gender)
            if 1 <= gender <= 3:
                break
            else:
                print(f'[@] "{gender}" não está entre as opções!')
        else:
            print(f'[@] \033[1;31m"{gender}" não é válido!\033[m')
    people.insert(i, dict(name=name, age=age, gender=gender))
    print(f'[@] Você deseja adicionar mais uma pessoa?')
    while True:
        add = input(f'[Y/N] >>> ')
        add = add.lower()
        if add in ['n', 'nao', 'não', 'no', 'y', 'sim', 'yes']:
            break
        else:
            print(f'[@] \033[1;31m"{add}" não é válido!\033[m')
    if add in ['n', 'nao', 'não', 'no']:
        break
    elif add in ['y', 'sim', 'yes']:
        i += 1

adult = 0
for a in range(0, len(people)):
    if people[a]['price'] >= 18:
        adult += 1

males = 0
for g in range(0, len(people)):
    if people[g]['gender'] == 1:
        males += 1

youngf = 0
for f in range(0, len(people)):
    if people[f]['gender'] == 2:
        if people[f]['price'] < 20:
            youngf += 1

print(f'[@] Analisando', end='')
for o in range(3):
    print(f'.', end='')
    sleep(.5)
print(f'.')
print(f'[@] Aqui está o resultado:')
print(f'[@] Foram cadastrados {adult} pessoas com 18 anos ou mais\n'
      f'[@] Foram cadastrados {males} homems\n'
      f'[@] Existem {youngf} mulheres com menos de 20 anos')
