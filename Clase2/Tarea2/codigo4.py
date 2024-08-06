nombre1 = str(input())
nombre2 = str(input())
n = int(input())

cont1 = 0
cont2 = 0

for i in range(n):
  ganador = str(input())
  if ganador == nombre1:
    cont1 += 1
  elif ganador == nombre2:
    cont2 += 1

if cont1 > cont2:
  print(nombre1)
elif cont2 > cont1:
  print(nombre2)
else:
  print('empate')