#programa que lee una frase introducida desde el teclado y la escriba al revés.
frase = input("Digite la frase: ")
cadena = ""
for i in range(len(frase),0,-1):
    cadena +=frase[i-1]
print (cadena)
