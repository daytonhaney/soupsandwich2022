
def userInput():

    firstname = input("Enter first name: \n ")
    lastName = input("Enter last name:  \n ")
    return firstname, lastName


def printName(name1, name2):
    print("Your Name is ", name1, name2)


def main():

    yourname, yourLastname = userInput()
    printName(yourname, yourLastname)


main()
