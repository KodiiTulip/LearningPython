n1 = (input('[@] Digite algo: '))

print(f'[@] Todas as informações disponíveis sobre {n1}:')

print(f'Classe: {type(n1)}\nAlfanumerico: {n1.isalnum()}\nAlfabético: {n1.isalpha()}')
print(f'Numérico: {n1.isnumeric()}\nMinúscula: {n1.islower()}\nMaiúscula: {n1.isupper()}')
print(f'Captalizado: {n1.istitle()}\nSomente espaços: {n1.isspace()}')
