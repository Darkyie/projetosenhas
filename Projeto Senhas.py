import hashlib, base64

from itertools import product as cp


def codificar_senha(senha):
    senha_encoded = senha.encode('utf-8')
    digest = hashlib.sha512(senha_encoded).digest()
    digest_b64_encoded = base64.b64encode(digest)
    digest_b43_encoded_utf8_decoded = digest_b64_encoded.decode('utf-8')
    return digest_b43_encoded_utf8_decoded

def gerarpalavras():
    counter = 0
    filepalavras = open('palavras.txt', 'r', encoding ='utf-8')
    linhas = filepalavras.readlines()
    cada1 = [0] * len(linhas)
    seila = [x.rstrip('\n') for x in linhas]
    for i in seila:
        cada1[counter] = i
        counter += 1
    return(cada1)


def potencial(lista_palavras):
    aux = []
    for x in [list(cp(lista_palavras, repeat=i)) for i in range(1,6)]:
        for j in range(len(x)):
            aux.append(' '.join(x[j]))
    return aux

palavras = gerarpalavras()
senhas = potencial(palavras)
codificadas = [0] * len(senhas)
for i in range(len(senhas)):
    codificadas[i] = codificar_senha(senhas[i])

filesenhas = open('usuarios_senhascodificadas.txt', 'r', encoding='utf-8')
linhas = filesenhas.readlines()
seila = [x.rstrip('\n') for x in linhas]

for linha in range(len(seila)):
    z = seila[linha].split(":")
    for i in range(len(codificadas)):
        if codificadas[i] == z[1]:
            senhasquebradas = open(("senhas_quebradas.txt"), "a")
            senhasquebradas.writelines("%s:%s\n" % (z[0], codificadas[i]))


