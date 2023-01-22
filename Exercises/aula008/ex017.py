from Libraries.numeric_check import isfloat
from math import sqrt, pow

# faça um programa que leia o comprimento do cateto oposto e do adjacente de um triangulo retangulo, calcule e mostre
# o valor da hipotenusa
print(f'[@] Insira o valor do cateto oposto:')
while True:
    co = input(f'>>> ')
    if isfloat(co):
        co = float(co)
        break
    else:
        print(f'[@] \033[1;31m"{co}" não é válido!\033[m')

print(f'[@] Insira o valor do cateto adjacente:')
while True:
    ca = input(f'>>> ')
    if isfloat(ca):
        ca = float(ca)
        break
    else:
        print(f'[@] \033[1;31m"{ca}" não é válido!\033[m')

hsq = pow(co, 2) + pow(ca, 2)
h = sqrt(hsq)
print(f'[@] o valor da hipotenusa com os catetos {co} e {ca} equivale a {h}')

