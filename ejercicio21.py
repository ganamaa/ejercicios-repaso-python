# programa que dado un número del 1 a 7 escriba el correspondiente nombre del día de la semana.

numero = int(input('Digite un numero ')) 
semana = {'Lunes': 1, 'Martes': 2, 'Miercoles': 3, 'Jueves': 4, 'Viernes': 5, 'Sabado': 6, 'Domingo': 7} 
llave = semana.keys() 
dia = semana.values() 
encontro = False 
for dia, llave in semana.items(): 
    if llave == numero & numero>=0: 
      print(f"El dia de la semana que seleccionaste es: {dia}") 
      encontro = True 
if (encontro == False): 
  print("Entrada incorrecta") 
