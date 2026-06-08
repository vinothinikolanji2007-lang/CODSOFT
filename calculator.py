def addition():

    print("Result:",a+b)
    
def subtraction():
    print("Result:",a-b)
def multiplication ():
    print("Result:",a*b)
def Division():
    print("Result:",a/b)
def modulo():
    print("Result:",a%b)
for i in range(6):
    a=int(input("Enter Your first number: "))
    print("Choose operation:")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. %")
    choice=input("")
    b=int(input("Enter  your second number:"))
    if choice=="+":
        addition()
    elif choice=="-":
        sub=subtraction()
    elif choice=="*":
        mult=multiplication()
    elif choice=="/":
        div=Division()
    elif choice=="%":
        mod=modulo()
    else:
        print("Invalid choice!!")
    
