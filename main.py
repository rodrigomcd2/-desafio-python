palavra = input("Escreva a palavra: ") # escreva a palavra
palavra_contrario = palavra[::-1]# funcão para inverter a palavra 

if palavra == palavra_contrario:# verfica se as palavras são iguais
    print(f"{palavra} é um palíndromo")
else:
    print(f"{palavra} não é um palíndromo")