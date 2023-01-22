from random import randint

# um sorteio aleatório entre 4 "strings"

students = ['', '', '', '']
print(f'[@] Digite para mim 4 nomes aleatórios, e apenas um deles será sorteado.')

for i in range(0, 4):
    students[i] = input(f'>>> ')
    print(f'[{i + 1}] = {students[i]}')

r = randint(0, 3)
print(f'[@] O nome sorteado foi: {students[r]}')
