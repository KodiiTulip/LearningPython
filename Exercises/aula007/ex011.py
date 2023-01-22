from Libraries.numeric_check import isfloat


# 1 l de tinta == 2 m²
print(f'[@] Me envie a altura e a largura de uma parede,')
print(f'[@] e lhe informarei quantos litros de tinta você ira precisar')
while True:
    h = input(f'A: ')
    if isfloat(h):
        h = float(h)
        break
    else:
        print(f'[@] \033[1;31m"{h}" não é válido!\033[m')
while True:
    w = input(f'L: ')
    if isfloat(w):
        w = float(w)
        break
    else:
        print(f'[@] \033[1;31m"{w}" não é válido!\033[m')

area = h * w
liters = area / 2
print(f'[@] Area: {area: .2f} m²')
print(f'[@] Litros de tinta: {liters: .2f} l')
