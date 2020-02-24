""" programa que imprime la media de los elementos que se encuentran en las posiciones pares y la media de los elementos que se encuentran en las posiciones impares de 
Universidad Distrital Francisco José de Caldas Ingeniería de Sistemas Programación Básica Ejercicios de programación básica
una tupla de enteros de 20 posiciones, (la tupla se declara arbitrariamente en el código). """

tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
numPar = 0
numImpar = 0

for i in range(0, len(tupla)):
    
    if(i % 2 == 0):
        
        numPar += tupla[i]
    else:
        numImpar += tupla[i]

print("La media de los elementos que se encuentrar en una posicion par es de: {}".format(numPar/10))
print("La media de los elementos que se encuentrar en una posicion impar es de: {}".format(numImpar/10))
