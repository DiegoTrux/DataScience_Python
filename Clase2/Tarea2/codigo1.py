x = int(input())
minimo  = x
maximo = x
suma = 0
n = 0
while x >= 0:
  n += 1
  suma += x
  if x < minimo:
    minimo = x
  if x > maximo:
    maximo = x
  x = int(input())

if n == 0:
  print('No hay datos')
else:
  print('n={}'.format(n))
  print('media={:.2f}'.format(suma/n))
  print('min={}'.format(minimo))
  print('max={}'.format(maximo))