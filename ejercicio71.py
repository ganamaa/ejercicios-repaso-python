#programa que muestra el numero de dias de un mes
def numeroDias(mes):
    if(mes==1):
        return "Enero y tiene 31 días"
    elif(mes==2):
        return "Febrero y tiene 28-29 días"
    elif (mes==3):
        return "Marzo y tiene 31 días"
    elif (mes==4):
        return "Abril y tiene 30 días"
    elif(mes==5):
        return "Mayo y tiene 31 días"
    elif (mes==6):
        return "Junio y tiene 30 días"
    elif (mes==7):
        return "Julio y tiene 31 días"
    elif (mes==8):
        return "Agosto y tiene 31 días"
    elif (mes==9):
        return "Septiembre y tiene 30 días"
    elif(mes==10):
        return "Octubre y tiene 31 días"
    elif (mes==11):
        return "Noviembre  y tiene 30 días"
    elif (mes==12):
        return "Diciembre y tiene 31 días"
    else:
        return "El numero que ingreso no corresponde con un mes"




mes =  int(input("Digite el mes: "))
print("El número de días del mes {} es: {}".format(mes,numeroDias(mes)))
