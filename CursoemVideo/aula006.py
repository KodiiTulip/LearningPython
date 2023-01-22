n1 = (input('[@] Digite um número: '))

print('Alfanumerico:', n1.isalnum(), '\nAlfabético:', n1.isalpha(), '\nNumérico:', n1.isnumeric())
print('Lowercase:', n1.islower(), '\nUppercase:', n1.isupper(), '\nClasse:', type(n1), '\n')

n2 = (input('[@] Digite um segundo número: '))

print('Alfanumerico:', n2.isalnum(), '\nAlfabético:', n2.isalpha(), '\nNumérico:', n2.isnumeric())
print('Lowercase:', n2.islower(), '\nUppercase:', n2.isupper(), '\nClasse:', type(n2), '\n')

if n1.isnumeric() and n2.isnumeric():
    n1 = float(n1)
    n2 = float(n2)
    s = n1 + n2
    print(f'[@] A soma entre {n1} e {n2} vale {s}')
else:
    print(f'[@] "{n1}" e/ou "{n2}" não é(são) numérico(s).')
