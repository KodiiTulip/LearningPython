# program pergunta a distância de uma viagem em km
# calcule o preço da passagem, cobrando RS$0.50 por km de viagens de até 200 km
# e RS$0.45 para viagens mais longas
from Libraries.numeric_check import isfloat

print(f'[@] digite a distancia da viagem:')
while True:
    dis = input(f'>>> ')
    if isfloat(dis):
        dis = float(dis)
        break
    else:
        print(f'[@] \033[1;31m"{dis}" não é válido!\033[m')
if dis > 200:
    print(f'[@] A viagem sendo maior do que 200 km, a tarifa será RS$0.45')
    tax = dis * 0.45
    print(f'[#] Preço da passagem: RS${tax:.2f}')
elif dis <= 200:
    print(f'[@] A viagem sendo menor ou igual a 200 km, a tarifa será RS$0.50')
    tax = dis * 0.5
    print(f'[#] Preço da passagem: RS${tax:.2f}')
