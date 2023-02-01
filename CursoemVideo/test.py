davi = ['Davi', 'davi', 'david', 'David']
jo = ['Joana', 'joana', 'joaninha', 'Joaninha']
nao = ['Não', 'Nao', 'não', 'nao', 'N', 'n']
sim = ['Sim', 'sim', 'si', 'Si', 'S', 's']
counter = 0
name = input(f'[@] Olá humano :)\n[@] Qual o seu nome? ')

print(f'[@] {name}...')
print(f'[@] Que belo nome, {name} :)')

friend = input('[@] Por acaso você tem algum amigo especial que deseja mencionar? ')

while True:
    if counter > 4:
        print(f'[@] Sinto muito, {name} :(\n[@] Mas chegamos ao meu limite.\n[@] Até a proxima vez! :)')
        exit()
    if friend in davi:
        print(f'[@] {friend}?\n[@] Que viadinho.')
        counter += 1
    elif friend in jo:
        print(f'[@] {friend}?\n[@] Que nome lindo :3')
        counter += 1
    elif friend in sim:
        friend = input(f'[@] Oh. Qual o nome dessa pessoa? ')
        if friend in davi:
            print(f'[@] {friend}?\n[@] Que viadinho.')
            counter += 1
        elif friend in jo:
            print(f'[@] {friend}?\n[@] Que nome lindo :3')
            counter += 1
        else:
            print(f'[@] {friend}?\n[@] Que nome bonito :)')
            counter += 1
    elif friend in nao:
        print(f'[@] Entendo.\n[@] Até a proxima vez, {name} :)')
        exit()
    else:
        print(f'[@] {friend}?\n[@] Que nome bonito :)')
        counter += 1
        friend = input(f'[@] Tem mais alguem especial que deseja mencionar? ')
