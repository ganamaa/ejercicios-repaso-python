# ejercicios con modulos .81
import aritmetica as arit

numeUno = int(input("ingrese un numero: "))
numeDos = int(input("ingrese un numero: "))

suma = arit.sumar(numeUno, numeDos)
resta = arit.restar(numeUno, numeDos)
multi = arit.multiplicar(numeUno, numeDos)
div = arit.dividir(numeUno, numeDos)
pot = arit.potencia(numeUno, numeDos)

print("para los numeros {} y {} \nsu suma es: {}\nsu resta: {}\nsu multiplicacion: {}\nsu division entera: {}\nsu potencia: {}".format(numeUno,numeDos,suma,resta,multi,div,pot))
