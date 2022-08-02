

# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e 
# depois faça uma chamada à função para listar os números      

'''
def imprimeNumerosPares():
    for i in range(2, 21, 2):
        print(i)

imprimeNumerosPares()
'''



# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string
'''
def letrasMinusculas(palavra):
    print(palavra.lower())
letrasMinusculas("LUGAR")

'''

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

'''
def listaEncrementada(arg1):
    arg1.append(5)
    arg1.append(6)

lista = [1,2,3,4]
listaEncrementada(lista)
print(lista)

'''



# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos