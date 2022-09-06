#sortear numeros aleatorios e dizer o maior e o menor
import random

num = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))

for i in num:
    print(f'{i} ', end='')

print()
print(f'Maior numero {max(num)}')
print(f'Menor numero {min(num)}')
