from Libraries.numeric_check import isfloat, isint

print(f'[@] Envie para mim as notas de um aluno (de 0 a 10):')

while True:
    print(f'[@] Quantas notas são?')
    qua = input(f'>>> ')
    if isint(qua):
        qua = int(qua)
        break
    else:
        print(f'[@] \033[1;31m{qua} não é válido!\033[m')

grade = []
for i in range(0, qua):
    while True:
        grade.insert(i, input(f'[{i+1}]: '))
        if isfloat(grade[i]):
            grade[i] = float(grade[i])
            if 10 >= grade[i] >= 0:
                break
            else:
                print(f'[@] \033[1;31m{grade[i]} não está entre 0 e 10!\033[m')
        else:
            print(f'[@] \033[1;31m{grade[i]} não é válido!\033[m')
            grade.pop(i)

media = sum(grade) / qua
print(f'[@] Aqui está a média: {media:.2f}')

if media < 5:
    print(f'[@] O aluno está \033[1;31mreprovado\033[m')
elif 6.9 > media >= 5:
    print(f'[@] O aluno está de \033[1;33mrecuperação\033[m')
elif media >= 7:
    print(f'[@] O aluno está \033[1;32maprovado\033[m')
