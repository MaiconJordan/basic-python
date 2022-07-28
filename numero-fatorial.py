# programa para achar numero fatorial
# fatorial só pode ser numero positivo e inteiro
# ex: fatorial de 3 = (3 * 2 * 1) = 6

numero = input("digite um numero ")
numerodois = int(numero)

if numerodois <= 0:
    print("digite apenas numeros positivos ")

    fatorial = 1
for fatorial in numerodois:
    fatorial = fatorial * numerodois
    print(fatorial)
