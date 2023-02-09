from Libraries.numeric_check import isint

note50 = 0
note20 = 0
note10 = 0
note5 = 0
note1 = 0

print(f'[@] Qual o valor a ser sacado?')
while True:
    value = input('>>> ')
    if isint(value):
        value = int(value)
        break
    else:
        print(f'[@] \033[1;31m"{value}" não é válido!\033[m')

if value >= 50:
    note50 = value // 50
    value = value % 50
if 50 > value >= 20:
    note20 = value // 20
    value = value % 20
if 20 > value >= 10:
    note10 = value // 10
    value = value % 10
if 10 > value >= 5:
    note5 = value // 5
    value = value % 5
if 5 > value >= 1:
    note1 = value

if note50 > 0:
    print(f'[@] {note50} notas de RS$50.00')
if note20 > 0:
    print(f'[@] {note20} notas de RS$20.00')
if note10 > 0:
    print(f'[@] {note10} notas de RS$10.00')
if note5 > 0:
    print(f'[@] {note5} notas de RS$5.00')
if note1 > 0:
    print(f'[@] {note1} notas de RS$1.00')
