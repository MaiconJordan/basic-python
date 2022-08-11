endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"


import re  # Regular Expression -- RegEx

# 5 dígitos + hífen (opcional) + 3 dígitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)
    
    

#validando padrão da URL

url = 'https://www.bytebank.com.br/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL não é válida.")

print("A URL é válida")