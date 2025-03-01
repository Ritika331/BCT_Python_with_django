email = ""  
password = ""  
data = []  

def su():
    global email, password
    database={}
    email = input("Enter email: ")
    password = input("Enter password: ")
    database["email"]=email
    database["password"]=password
    data.append(database)
    print("Signup successful!")
def si():
    n=len(data)
    email=input("Enter email")
    password=input("Enter password")
    for i in range(n):
        if data[i]['email']!=email:
            print("You are not registered")
        else:
            if data[i]['password']!=password:
                print("Incorrect password")
            else:
                print("Login Successful")
def main():
    while True:
        c = input("\n1. Sign Up\n2. Sign In\n3. Exit\nEnter choice: ")
        if c == '1':
            su()
        elif c == '2':
            si()
        else:
            print("Goodbye!")
            break
if __name__== "__main__":
    main()