x = input("Enter Name: ")
y = input("Enter Password: ")
z = input("Enter Password again: ")


if y == z:
    if len(y) >= 8 or len(z) >= 8:
        print("Passwords must be at least 8 characters long: ")
    else:
        print("Thank you, account made: ")

else:
    print("Passwords do not match - please try again")
