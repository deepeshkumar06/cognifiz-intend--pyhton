str = input("Enter the String to Reverse : ")

def rev(name):
    return name[::-1]

revstr = rev(str)

print("The orginal String is : ",str)
print("The reversed String is : ",revstr)