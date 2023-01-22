from Libraries.numeric_check import isfloat
from math import sin, cos, tan, radians

# crie um programa que leia um angulo qualquer e mostre seu seno cosseno e tangente

print(f'[@] Insira um ângulo qualquer e lhe direi seu seno, cosseno e tangente.')
while True:
    n = input(f'>>> ')
    if isfloat(n):
        n = float(n)
        break
    else:
        print(f'[@] \033[1;31m"{n}" não é válido!\033[m')

r = radians(n)
s = sin(r)
c = cos(r)
t = tan(r)

print(f'[@] Senoº{n} = {s:.2f}\n[@] Cossenoº{n} = {c:.2f}\n[@] Tangenteº{n} = {t:.2f}')
