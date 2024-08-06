x = float(input()) + 0.01
x = int(x*100)
x = x - x%10

mon1 = int(x/100)
x = (x%100)
print(mon1, ' monedas de s/.1.00')
#print(x)
mon0_5 = int(x/50)
x = (x%50)
print(mon0_5, ' monedas de s/.0.50')
mon0_2 = int(x/20)
x = (x%20)
print(mon0_2, ' monedas de s/.0.20')
mon0_1 = int(x/10)
x = (x%10)
print(mon0_1, ' monedas de s/.0.10')



