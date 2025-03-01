n=int(input("Enter the number to find factorial"))
s=lambda a:1 if a==0 else a*s(a-1)
print("Factorial is",s(n))