#programa que iniciar um numero de 1 a 10 e o usuario deve acertar, o programa diz se ele chutou um numero a cima ou abaixo


#numero = numero sorteado 1 a 10
#acertou = false

# enquanto aceritou = falso
#chute = usuario digita um valor
#if chute for maior numero imprime "chute maior que numero"
#if  chute < numero
#  "chute menor que numero"
#if chute == numero
#   print "voce acertou"
#   acertou = true
#else
# voce digitou um numero invalido
import random

numero_sorteado = random.randint(1, 10)
rodada = 1
tentativas = 3

while (rodada <= tentativas):    
    print("tentativa {} de {}".format(rodada, tentativas))
    chute = int(input("Digite um numero de 1 a 10: "))
    if (chute > numero_sorteado):
        print("Numero chutado é acima do sorteado")
    elif (chute < numero_sorteado):
        print("Número chutado é abaixo do numero sorteado")
    elif (chute == numero_sorteado):
        print("Você acertou")
    print("*****************************")
    rodada += 1
        
print("FIM DE JOGO")    



