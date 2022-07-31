# programa para achar numero fatorial
# fatorial só pode ser numero positivo e inteiro
# ex: fatorial de 3 = (3 * 2 * 1) = 6

numero = int(input("digite um numero "))


if numero > 0:
    fatorial = 1
    for item in range(1, numero + 1):
        fatorial = fatorial * item
    print(fatorial)
else:
    print("Digite um numero inteiro maior que zero")




