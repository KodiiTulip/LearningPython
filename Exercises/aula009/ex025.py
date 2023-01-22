# um programa que leia o nome completo de uma pessoa e mostre:
# o nome em capslock
# nome com todas as letras minusculas
# quantas letras ao todo sem considerar os espaços
# quantas letras tem o primeiro nome
# detectar se tem silva no nome

print(f'[@] digite seu nome completo:')
name = input(f'>>> ')
name = name.title()
print(f'\n[@]: {name}')

name1 = name.upper()
print(f'[@]: {name1}')

name2 = name.lower()
print(f'[@]: {name2}')

name3 = len(name) - name.count(' ')
print(f'[@]: {int(name3)}')

name4 = name.find(' ')
print(f'[@]: {int(name4)}')

if 'Silva' in name:
    print(f'[@]: Você tem o nome Silva :)')
