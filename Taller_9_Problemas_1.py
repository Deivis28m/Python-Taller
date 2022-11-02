def getListOfLengths(frases):
    lista_frase = list(frases.split())
    return list(map(len,lista_frase ))
    
N = int(input(""))
for i in range(N):
    frases = input("")
    print(getListOfLengths(frases))
