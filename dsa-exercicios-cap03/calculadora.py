print("************** Python Calculadora **************\n")
print("Selecione o número da operação desejada")
print("1 - Soma")
print("2 - Subtração")
print("1 - Multiplicação")
print("1 - Divisão")

operacao = int(input("Digite sua opção (1/2/3/4)\n"))

primeiro = int(input("Digite o primeiro numero\n"))
segundo = int(input("Digite o Segundo numero\n"))

if operacao == 1:
    print(f'{primeiro} +  {segundo} =  {primeiro + segundo}')
else:
    pass
