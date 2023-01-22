davi = ['Davi', 'davi', 'david', 'David']
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
        print(f'[@] {friend}?\n[@] Que viadinho.\n[@] Desculpe-me. Eu não deveria falar algo assim.')
        counter += 1
    else:
        if friend in sim:
            friend = input(f'[@] Oh. Poderia me dizer o nome dessa pessoa?')
            print(f'[@] {friend}?\n[@] Que nome bonito :)')
            counter += 1
        else:
            if friend not in nao:
                print(f'[@] {friend}?\n[@] Que nome bonito :)')
                counter += 1
    if friend in nao:
        print(f'[@] Entendo.\n[@] Até a proxima vez, {name} :)')
        exit()
    if friend not in sim:
        friend = input(f'[@] Tem mais alguem especial que deseja mencionar? ')
