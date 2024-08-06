n = str(input())
col = n[0]
num = int(n[1])

if col == 'a' or col == 'c' or col == 'e' or col == 'g':
  if num % 2 == 0:
    print('blanco')
  else:
    print('negro')
else:
  if num % 2 == 0:
    print('negro')
  else:
    print('blanco')