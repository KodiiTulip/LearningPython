from Libraries.numeric_check import isfloat

print(f'[@] Digite o peso de uma pessoa:')
while True:
    peso = input(f'>>> ')
    if isfloat(peso):
        peso = float(peso)
        break
    else:
        print(f'[@] \033[1;31m"{peso}" não é válido!\033[m')
print(f'[@] Digite a altura de uma pessoa:')
while True:
    alt = input(f'>>> ')
    if isfloat(alt):
        alt = float(alt)
        break
    else:
        print(f'[@] \033[1;31m"{alt}" não é válido!\033[m')

imc = peso / (alt ** 2)
if imc < 18.5:
    print(f'[@] O IMC dessa pessoa é de {imc}, indicando que elu está abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'[@] O IMC dessa pessoa é de {imc}, indicando que elu está com peso ideal.')
elif 25 <= imc < 30:
    print(f'[@] O IMC dessa pessoa é de {imc}, indicando que elu está com sobrepeso.')
elif 30 <= imc < 40:
    print(f'[@] O IMC dessa pessoa é de {imc}, indicativo de obesidade.')
elif 40 <= imc:
    print(f'[@] O IMC dessa pessoa é de {imc}, indicativo de obesidade mórbida.')
