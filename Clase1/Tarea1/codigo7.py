x = float(input())
y = int(input())

x = x * 0.8

x = x - 7 * y

n = int(x/y)

tramo1 = 0
tramo2 = 0
tramo3 = 0
tramo4 = 0
tramo5 = 0

if n <= 5:
    tramo1 = (x-0*y) * 0.08
elif n <= 20:
    tramo1 = 5 * y * 0.08
    tramo2 = (x-5*y) * 0.14
elif n <= 35:
    tramo1 = 5 * y * 0.08
    tramo2 = 15 * y * 0.14
    tramo3 = (x-20*y) * 0.17
elif n <= 45:
    tramo1 = 5 * y * 0.08
    tramo2 = 15 * y * 0.14
    tramo3 = 15 * y * 0.17
    tramo4 = (x-35*y) * 0.20
elif n > 45:
    tramo1 = 5 * y * 0.08
    tramo2 = 15 * y * 0.14
    tramo3 = 15 * y * 0.17
    tramo4 = 10 * y * 0.20
    tramo5 = (x-45*y) * 0.30
    
tramo = tramo1 + tramo2 + tramo3 + tramo4 + tramo5

print( '%.2f' % tramo)