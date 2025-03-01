n=int(input("Enter a number"))

x=n

c=0

while(x>0):

 r=0

 r=x%10

 c=c+r*r*r

 x=x//10

if c==n:

 print("Armstrong")

else:

 print("Not Armstrong")
