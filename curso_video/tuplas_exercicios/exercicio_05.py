


listagem = ('Caderno', 2.00,
            'Livro', 40.00,
            'Borracha', 2.50,
            'Lapis', 1.00)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for itens in range(0, len(listagem)):
    if itens % 2 == 0:
        print(f'{listagem[itens]:.<30}', end ='')
    else:
        print(f'R${listagem[itens]:>7.2f}')
print('-' * 40)