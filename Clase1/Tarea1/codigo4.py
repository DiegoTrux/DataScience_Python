v = float(input())
t = float(input())

x_t = v * t * 1/(2**(0.5))
y_t = v * t * 1/(2**(0.5)) - 1/2 * 9.8 * (t**2)

print(x_t)
print(y_t)