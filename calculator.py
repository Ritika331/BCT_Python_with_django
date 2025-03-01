def add(a,b):
 return a+b
def sub(a,b):
 return a-b
def multiply(a,b):
 return a*b
def div(a,b):
 return a/b
def mod(a,b):
 return a%b
def power(a,b):
 return a**b
print("Enter your choice")
x=int(input("Enter 1 to add \nEnter 2 to subtract \nEnter 3 to multiply \nEnter 4 to divide \nEnter 5 to calculate modulus \nEnter  6 for power\n"))
a=int(input("Enter first number"))
b=int(input("Enter second number"))
if x==1:
    answer= add(a,b)
elif x==2:
    answer=sub(a,b)
elif x==3:
    answer=multiply(a,b)
elif x==4:
    answer=div(a,b)
elif x==5:
    answer=mod(a,b)
else:
    answer=power(a,b)
print(answer)
    
