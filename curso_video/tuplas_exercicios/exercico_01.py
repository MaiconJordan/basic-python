#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vonte
#Seu Programa devera ler um numero pelo teclado (entre 0 a 20) e mostra-lo por extenso

extensos = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartoze','quinze','dezeseis','dezessete','dezoito','dezenove','vinte')


while True:    
    entrada = int(input('Digite um numero de entre 0 e 20: '))
    if 0 <= entrada <= 20:
        break
print(f'Você digitou o numero {extensos[entrada]}')
