# programa que dada una tupla de las vocales y otra con las consonantes, capture una cadena de caracteres y cuente cuantos caracteres pertenecen a la tupla de vocales, cuantos a la tupla de consonantes y cuantos no pertenecen a ninguna de las dos tuplas.
consonantes = ("B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "Ñ", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z")
vocales = ("A","E","I","O","U")

cadena = input("Digite la cadena de caracteres: ")
consonantesNum = 0
vocalesNum = 0
ningunpNum = 0

for x in cadena.upper():
    for y in vocales:
        if(x==y):
            vocalesNum +=1
    for y in consonantes:
        if(x==y):
            consonantesNum +=1

ningunpNum = len(cadena) - consonantesNum - vocalesNum

print("para la cadena {}, se econtraron un numero de consonantes de: {}".format(cadena,consonantesNum))
print("Un numero de vocales de  {} y ninguna de estas: {}".format(vocalesNum,ningunpNum))
