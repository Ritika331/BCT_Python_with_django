n=int (input("enter a number to check palindrome "))

x=n

d=0

rev=0

while (n>0):

 d=0

 d=n%10

 n=n//10

 rev=rev*10+d

if rev==x:

 print("the numner is palindrome")

else:

 print("the number is not palindrome")
