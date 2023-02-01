from time import sleep
from Libraries.numeric_check import isint


people = []
for i in range(4):
    print(f'-----[{i + 1}º Pessoa]-----')
    print(f'[@] Qual o seu nome?')
    name = input(f'>>> ')
    print(f'[@] Qual a sua idade?')
    while True:
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
    while True:
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

mediaage = []
for a in range(0, len(people)):
    mediaage.insert(a, people[a]['age'])
media = sum(mediaage) / len(mediaage)

males = []
for g in range(0, len(people)):
    if people[g]['gender'] == 1:
        males.insert(g, people[g])

oldestm = males[0]['age']
oldestmindex = 0
for m in range(0, len(males)):
    if males[m]['age'] > oldestm:
        oldestm = males[m]['age']
        oldestmindex = m

youngf = 0
for f in range(0, len(people)):
    if people[f]['gender'] == 2:
        if people[f]['age'] < 20:
            youngf += 1

print(f'[@] Analisando', end='')
for o in range(3):
    print(f'.', end='')
    sleep(.5)
print(f'.')
print(f'[@] Aqui está o resultado:')
print(f'[@] A média de idade do grupo é: {media} anos\n'
      f'[@] O homem mais velho é {males[oldestmindex]["name"]} com {oldestm} anos\n'
      f'[@] Existem {youngf} mulheres com menos de 20 anos')
