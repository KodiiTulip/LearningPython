
print(f'[@] Envie para mim um número para visualizar sua tabuada.')
while True:
    n = (input('>> '))
    if n.isnumeric():
        n = int(n)
        break
    else:
        print(f'[@] \033[1;31m"{n}" não é válido\033[m')
for i in range(0, 11):
    print(f"{f'{n: >2} * {i: <2} = {n * i: <3}': ^21}")
