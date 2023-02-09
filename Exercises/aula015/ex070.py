from time import sleep
from Libraries.numeric_check import isint

i = 0
produto = []
while True:
    print(f'-----[{i + 1}º Produto]-----')
    name = input(f'[@] Nome: ')
    while True:  # price
        price = input(f'[@] Preço: RS$')
        if isint(price):
            price = int(price)
            break
        else:
            print(f'[@] \033[1;31m"{price}" não é válido!\033[m')
    produto.insert(i, dict(name=name, age=price))
    print(f'[@] Você deseja adicionar mais um produto?')
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

total = 0
for a in range(0, len(produto)):
    total += produto[a]['price']

expen = 0
for g in range(0, len(produto)):
    if produto[g]['price'] >= 1000:
        expen += 1

cheap = 0
for f in range(0, len(produto)):
    if produto[f]['gender'] == 2:
        if produto[f]['price'] < 20:
            cheap += 1

print(f'[@] Analisando', end='')
for o in range(3):
    print(f'.', end='')
    sleep(.5)
print(f'.')
print(f'[@] Aqui está o resultado:')
print(f'[@] Foram cadastrados {total} pessoas com 18 anos ou mais\n'
      f'[@] Foram cadastrados {expen} homems\n'
      f'[@] Existem {cheap} mulheres com menos de 20 anos')
