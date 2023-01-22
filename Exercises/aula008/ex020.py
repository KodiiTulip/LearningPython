from random import randint

# um sorteio aleatório entre 4 "strings" e uma ordem aleatoria

students = ['', '', '', '']
print(f'[@] Digite para mim 4 nomes aleatórios, e deles serão ordenados aleatoriamente.')

for i in range(0, 4):
    students[i] = input(f'>>> ')
    print(f'[{i + 1}] = {students[i]}')


r1 = randint(0, 3)
print(f'\n[1º]: {students[r1]}')
while True:
    r2 = randint(0, 3)
    if r2 != r1:
        print(f'[2º]: {students[r2]}')
        break
while True:
    r3 = randint(0, 3)
    if r3 != r1 and r3 != r2:
        print(f'[3º]: {students[r3]}')
        break
while True:
    r4 = randint(0, 3)
    if r4 != r1 and r4 != r2 and r4 != r3:
        print(f'[4º]: {students[r4]}')
        break
