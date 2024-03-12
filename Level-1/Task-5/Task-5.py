str = input("Enter the String to Reverse : ")

def rev(name):
    return name[::-1]

strev = rev(str)

if(str == strev):
    print("The Given String is Palindrome.")
else:
    print("The Given String is Not Palindrome.")