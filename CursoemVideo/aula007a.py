n1 = float(input('1: '))
n2 = float(input('2: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
p = n1 ** n2
print(f"{'Soma': <5}{'Multiplicação': ^15}{'Divisão': ^15}{'Divisão Inteira': ^15}{'Resto': ^15}{'Potência': >5}")
print(f"{s: <5.1f}{m: ^15.1f}{d: ^15.1f}{di: ^15}{r: ^15}{p: >5.1f}")
# desafio 005
n3 = float(input('um terceiro valor: '))
su = n3 + 1
an = n3 - 1
print(f"{f'Antecessor: {an}': <15}{f' Sucessor: {su}': >15}")
# desafio 006
n4 = float(input('agr um quarto numero: '))
do = n4 * 2
tr = n4 * 3
rq = n4 * .5

print(f"{f'dobro: {do}': <10}{f' triplo: {tr}': ^10}{f' raiz quadrada: {rq}': >5}")
# desafio 007
grade1 = float(input('\nagr me envie duas notas de prova:\n1: '))
grade2 = float(input('2: '))
media = (grade1 + grade2) / 2
print(f'media: {media}')
# desafio 008
meters = float(input('\nagr me envie um valor de medida em metros: '))
centi = meters * (10**2)
milim = meters * (10**3)
print(f"{f'Centimetros: {centi} cm': <15}{f'Milímetros: {milim} mm': >15}")
# desafio 009
n5 = float(input('\nagr me envie mais um número: '))
for i in range(0, 11):
    print(f"{f'{n5} * {i} = {n5 * i}'}")
# desafio 010
# US$1.00 == RS$5.34
money = float(input('\nquanto dinherio vc tem? RS$'))

dollar = money / 5.34
print(f'Voce tem, em dolares: US${dollar: .2f}')
# desafio 011
# 1 l de tinta == 2 m²
h = float(input(f'\nAltura: '))
w = float(input(f'Largura: '))

area = h * w
liters = area / 2
print(f"{f'Area: {area: .2f} m²': <10}{f'Litros de tinta: {liters: .2f} l': >10}")
# desafio 012
price = float(input('\nPreço sem o desconto: RS$'))

new_price = price - (price * .05)
print(f'Novo preço com 5% de desconto: RS${new_price: .2f}')
# desafio 013
paycheck = float(input(f'\nSalário base: RS$'))

n_paycheck = paycheck + (paycheck * 1.15)
print(f'Novo salárioo com aumento: RS${n_paycheck: .2f}')
