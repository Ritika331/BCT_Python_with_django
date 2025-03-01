email = ""  
password = ""  
data = []  

def su():
    global email, password  
    database={}
    email = input("Enter email: ")
    if email.endswith(".com"):
        password = input("Enter password: ")
        database["email"]=email
        database["password"]=password
        data.append(database)
        print("Signup successful!")
    else:
        print("Invalid details")
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
def show_data():
    for i in data:
        print(i)
def main():
    while True:
        c = input("\n1. Sign Up\n2. Sign In\n3. Exit\n4. Show All Users\nEnter choice: ")
        if c == '1':
            su()
        elif c == '2':
            si()
        elif c == '3':
            print("Goodbye!")
            break
        elif c == '4':
            show_data()
        else:
            print("Enter 1, 2, 3, or 4.")

if __name__== "__main__":
    main()