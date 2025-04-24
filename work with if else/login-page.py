Un=str(input("Enter your Username: "))
Pw=str(input("Enter your password: "))

Unp="Shrilesh-Dhobale"
Pwp="Shri@123"

if (Un==Unp and Pw==Pwp):
    print("Successfully Login")

elif(Un!=Unp):
    print("Incorrect Username")

elif(Pw!=Pwp):
    print("You Enter Incorrect password, Please try again!")

else:
    print("Both are Incorrect")
