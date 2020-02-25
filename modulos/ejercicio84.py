# ejercicios con modulos .84
import aritmeticaOct as aOct

numeUno = int(input("ingrese un numero octal: "),8)
numeDos = int(input("ingrese un numero octal: "),8)

suma = aOct.sumarOct(numeUno, numeDos)
resta = aOct.restarOct(numeUno, numeDos)
multi = aOct.multiplicarOct(numeUno, numeDos)
div = aOct.dividirOct(numeUno, numeDos)

print("para los numeros {} y {} \nsu suma es: {}\nsu resta: {}\nsu multiplicacion: {}\nsu division entera: {}".format(oct(numeUno),oct(numeDos),suma,resta,multi,div))

