from time import sleep
from Libraries.numeric_check import isfloat

i = 0
produto = []
while True:
    print(f'-----[{i + 1}º Produto]-----')
    name = input(f'[@] Nome: ')
    while True:  # price
        price = input(f'[@] Preço: RS$')
        if isfloat(price):
            price = float(price)
            break
        else:
            print(f'[@] \033[1;31m"{price}" não é válido!\033[m')
    produto.insert(i, dict(name=name, price=price))
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

cheapest = produto[0]['price']
cheapindex = 0
for m in range(0, len(produto)):
    if produto[m]['price'] < cheapest:
        cheapest = produto[m]['price']
        cheapindex = m


print(f'[@] Analisando', end='')
for o in range(3):
    print(f'.', end='')
    sleep(.5)
print(f'.')
print(f'[@] Aqui está o resultado:')
print(f'[@] Gasto total RS${total}\n'
      f'[@] {expen} produtos custam mais do que RS$1000.00\n'
      f'[@] O produto {produto[cheapindex]["name"]} é o mais barato no carrinho.')
