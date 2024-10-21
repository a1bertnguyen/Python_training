import random 
#tao mot so ngau nhien tu 0 den 9 
x = random.randint(0, 9)
print (x)
#tao mot so ngau nhien tu 0.0 den 1.0
y= random.random()
print(y)
#tao mot chuoi ngau nhien voi do dai la 5 
z=''.join(random.choices('abcdefghijklmnopqrstuvwxyz',k=5))
print(z)