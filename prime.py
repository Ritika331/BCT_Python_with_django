n=int(input("enter a number to check prime "))

c=0

for i in range(1,n):

 if n%i== 0:

  c=c+1

if c<2:

 print (" it is a prime number")

else:

 print("it is not a prime number")
