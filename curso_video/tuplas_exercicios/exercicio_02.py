'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do brasileirao na ordem de colocação e depois mostre.
# Os 5 primeiro colocados
# Os ultimos 4 colocados
# time em ordem alfabetica
# Em que posição está o Flamengo
'''


from time import time


times = ("Palmeiras","Flamengo","Corinthians","Internacional","Fluminense","Athletico-PR","Atlético-MG","América-MG","Santos","Bragantino","Fortaleza","Botafogo","São Paulo",
"Ceará SC","Cuiabá","Coritiba","Avaí","Atlético-GO","Juventude")

print(times)
print()
print(f'Os primeiros cinco times: {times[0:5]} ')
print()
print(f'Os ultimos 4 times {times[-4:]}')
print(f'O Flamengo está na posição {times.index("Flamengo") + 1}ª')






