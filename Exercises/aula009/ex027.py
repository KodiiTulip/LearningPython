
print(f'[@] digite seu nome completo:')
name = input(f'>>> ')
name = name.title()
print(f'\n[@]: {name}')
name1 = name.split()
print(f'[@] Primeiro: {name1[0]}')
print(f'[@] Último: {name1[len(name1) - 1]}')
