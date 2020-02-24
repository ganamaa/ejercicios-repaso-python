#programa que dice si una frase es o no un palíndromo, es decir, si se lee igual de derecha a a izquierda que de izquierda a derecha.
frase = input("Digite la frase: ")
aux = 0
igual = 0
for ind in reversed(range(0, len(frase))):
  if frase[ind].lower() == frase[aux].lower():
    igual += 1
  aux += 1
if len(frase) == igual:
  print("la frase es palindroma")
else:
  print("la frase no es palindroma")
