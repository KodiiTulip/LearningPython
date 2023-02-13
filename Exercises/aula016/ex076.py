lista = ('a', 1.75,
         'b', 21.5,
         'c', 10.0,
         'd', 5.25,
         'e', .5)

print(f'■'*42)
print(f'LISTAGEM DE PRODUTOS')
print(f'■'*42)
for i in range(0, len(lista), 2):
    print(f'{lista[i]:.<30}' + f'RS$ {lista[i+1]: >7.2f}')
print(f'■'*42)
