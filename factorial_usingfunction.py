def mul(n):
    if n>0:
        return n*mul(n-1)
    else:
        return 1
x=int(input("Enter a value upto which multiplication is required"))
answer=mul(x)
print("Answer",answer)