# pragrama que calcula el area y longitud de una circunferencia

import math
radio = int(input("Ingrese el radio de la circunferencia:  "))
area = math.pi * math.pow(radio,2)
longitud = 2 * math.pi * radio

print("para un radio de {}, el area es: {} y su longitud es: {}".format(radio,area,longitud))
    
