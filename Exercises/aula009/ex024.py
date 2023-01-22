# programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
print(f'[@] Digite o nome de uma cidade:')
city = input(f'>>> ')

if 'Santo' in city.title()[:5]:
    print(f'[@] {city.title()} começa com "Santo"? Sim')
else:
    print(f'[@] {city.title()} começa com "Santo"? Não')
