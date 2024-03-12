def Validate(email):
    if "@" in email and "." in email.split("@")[-1]:
        return True
    else:
        return False
    
email = input("Enter the Mail to Validate : ")
value = Validate(email)

if(value == True):
    print("You Enter the correct Mail.....")

else:
    print("You Enter the Wrong Mail.....")