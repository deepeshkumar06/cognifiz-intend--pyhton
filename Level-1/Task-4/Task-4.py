while True:
    first_no = float(input("Enter the First Number : "))
    second_no = float(input("Enter the Second Number : "))

    ch = int(input("Enter the Choices (1.Addition , 2.Subtraction , 3.Multiplication , 4.Division , 5.Modulo) : "))

    if ch in (1, 2, 3, 4, 5):
        if ch == 1:
            print(f"The Addition of Two numbers is {first_no + second_no}.")
        elif ch == 2:
            print(f"The Subtraction of Two numbers is {first_no - second_no}.")
        elif ch == 3:
            print(f"The Multiplication of Two numbers is {first_no * second_no}.")
        elif ch == 4:
            if second_no == 0:
                print("Error! Division by zero is not allowed.")
                break
            print(f"The Division of Two numbers is {first_no / second_no}.")
        elif ch == 5:
            if second_no == 0:
                print("Error! Division by zero is not allowed.")
                break
            print(f"The Modulo of Two numbers is {first_no % second_no}.")
    else:
        print("You Entered the Wrong Choice...")

    another_calc = input("Do you want another calculation (Yes/No) : ").upper()

    if another_calc == "NO":
        break
