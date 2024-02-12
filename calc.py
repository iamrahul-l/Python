user_Ip_1= input("Please enter the first number: ")
if not user_Ip_1.isdigit():
    print(f"The entered {user_Ip_1} is invalid")
    exit(1)
user_Ip_2 = input("Please enter the second number: ")
if not user_Ip_2.isdigit():
    print(f"The enterd {user_Ip_2} is invalid")
    exit(1)
   
def Addition (user_Ip_1, user_Ip_2):
    tempadd=int(user_Ip_1)+int(user_Ip_2)
    print(f" \n The Addition of  {user_Ip_1} and {user_Ip_2} \n is {tempadd}")
    return tempadd

def Subtraction(user_Ip_1, user_Ip_2):
    tempSub=int(user_Ip_1)-int(user_Ip_2)
    print(f" \n The Subtraction of  {user_Ip_1} and {user_Ip_2} \n is {tempSub}")

def Multiply(user_Ip_1, user_Ip_2):
    tempmul=int(user_Ip_1)*int(user_Ip_2)
    print(f" \n The Multiplication of  {user_Ip_1} and {user_Ip_2} \n is {tempmul}") 
    return tempmul

def Divide(user_Ip_1, user_Ip_2):
    tempdiv=int(user_Ip_1)/int(user_Ip_2)
    tempmod=int(user_Ip_1)%int(user_Ip_2)
    print(f" \n The Division of  {user_Ip_1} and {user_Ip_2} \n is {tempdiv}")  
    print(f" \n The Modulus of  {user_Ip_1} and {user_Ip_2} \n is {tempmod}")      


tempadd=Addition (user_Ip_1, user_Ip_2)
Subtraction(user_Ip_1, user_Ip_2)
tempmul=Multiply(user_Ip_1, user_Ip_2)
Divide(user_Ip_1, user_Ip_2)

if tempmul > tempadd :
    print(f"\n The Multiplication value {tempmul} is > The addition value {tempadd} \n")

            