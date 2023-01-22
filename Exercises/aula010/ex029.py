# programa que leia a velocidade de um carro
# se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que foi multado
# a multa custará RS$7.00 por cada km/h acima do limite
from Libraries.numeric_check import isfloat

print(f'[@] Digite a velocidade do carro:')

while True:
    v = input(f'>>> ')
    if isfloat(v):
        v = float(v)
        break
    else:
        print(f'[@] \033[1;31m"{v}" não é válido!\033[m')

if v <= 80:
    print(f'[@] Este carro estava a {v} km/h que é dentro do limite de 80 km/h')
    print(f'[@] Portanto não haverá multa.')
elif v > 80:
    print(f'[@] Este veículo estava {v - 80:.2f} km/h acima do limite!')
    multa = (v - 80) * 7
    print(f'[@] Haverá uma multa de RS${multa:.2f}.')
    if multa < 1:
        print(f'[@] Como a multa é menor do que RS$1.00 ela pode ser ignorada com segurança.')
