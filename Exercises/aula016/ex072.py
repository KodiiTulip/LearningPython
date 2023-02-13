from Libraries.numeric_check import isint

num = ('Zero',
       'Um',
       'Dois',
       'Três',
       'Quatro',
       'Cinco',
       'Seis',
       'Sete',
       'Oito',
       'Nove',
       'Dez',
       'Onze',
       'Doze',
       'Treze',
       'Catorze',
       'Quinze',
       'Dezeseis',
       'Dezesete',
       'Dezoito',
       'Dezenove',
       'Vinte')

print(f'[@] Digite um número de 0 a 20')
while True:
    numind = input(f'>>> ')
    if isint(numind):
        numind = int(numind)
        if 0 <= numind <= 20:
            break
        else:
            print(f'[@] \033[1;31m"{numind}" não é válido!\033[m')
    else:
        print(f'[@] \033[1;31m"{numind}" não é válido!\033[m')
print(f'[@] Seu número por extenso é: {num[numind]}')
