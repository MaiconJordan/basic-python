from re import A


def jogar():
    
    print("********************************")
    print("********** Jogo Forca **********")
    print("********************************")
    
    arquivo = open("palavras.txt", "r")    
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)        
    arquivo.close()
    
    print(palavras)
    
    palavra_secreta = "cabecuda".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    enforcou = False
    acertou = False
    erros = 0
    
    print(letras_acertadas)    
    
    while (not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        
        if (chute in palavra_secreta):        
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
            
        else:
            erros += 1 

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        
        
    if (acertou):
        print("VOCÊ GANHOU ^_^ ")
    else:
        print("VOCÊ PERDEU")
    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()