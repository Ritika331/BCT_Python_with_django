a=int(input("Enter first number"))
b=int(input("Enter second number"))
r=lambda a,b:a if a>b else b
print("Greater number is",r(a,b))