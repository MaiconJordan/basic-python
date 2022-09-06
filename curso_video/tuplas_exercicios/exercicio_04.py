num = (int(input('Digite um numero: ')),
       int(input('Digite mais numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite ultimo numero: ')))

print(num)
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 2 apareceu na {num.index(3)+1}ª posição')
else:
    print('o Valor 3 nao foi digitado')

print('Os valores pares digitados foram: ', end = '')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')