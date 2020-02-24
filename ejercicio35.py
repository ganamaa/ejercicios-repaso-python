#programa que calcula el factorial de un número
def factorial(numero):
    factorial_num = 1
    while(numero>0):
        factorial_num *=  numero
        numero -=1
    return factorial_num

print(factorial(5))
