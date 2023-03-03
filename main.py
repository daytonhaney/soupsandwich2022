""" Still Work to be done """
from time import sleep
import pyfiglet

auditor = []
price_per_square_foot = float(.50)

total_services = {
        "Regular" : "General\nTidying\nSweep\nDust\nMop",
        "Premium" :"Regular Service + \nBathroom\nCloset\nSenior\nDiscount",
        "Outdoor": "Mowing\nPruning\nWeedWhacking\nSenior\nDiscount"
    }

def my_greeting():
    # about _, like placeholder
    opening_hint = \
        "*** Please adjust screen to wide for best picture ***\n\n\n "

    my_name, my_date, my_class = "Jason Pr*&%785au", "9 July 2022", "CMIS-120\n\n\n"
    for _ in my_name, my_date, my_class:  # '_' is a throw away variable, The compiler will use it once and forget
        # about _, like placeholder
        print(_)
    print(opening_hint.center(90))


def user_interface():
    """ This function is the customer display model"""
    sp = ''
    lines = "="*78

    # Line 18 to approx line 40 is code from previous weeks, put on wide view for best views
    print(lines)
    print(lines)
    # trying to maintain P#P8 Standard 78 characters
    print("="*22, "**Welcome to In & Out Services**", "="*22)
    print(lines)
    print(lines)

    regular = "Regular Service - Premium Service - Outdoor Service \n\n"

    print('')
    print(regular.center(81), end='')
    print(sp)  # old code but I like how it looks
    print("\t\tRegular  \t\t\tPremium")
    print(" \t\t -General Tidying  \t\t -Includes Bed / Bath +\n\t\t -Dust Mop Sweep  \t\t -Closets\t\t\t  \n\t\t\t   \t\t\t -1/2 Price Next Visit")
    print(sp)
    print(sp)
    print("\t\tOutdoor "  # qqqqq
          "Services "
          "Include: \n"
          "\t\t-Mowing \n"
          "\t\t-Pruning \n"
          "\t\t-Weed-Wacking \n"
          "\t\t-Pressure Wash \n"
          "\t\t-$100.00 \n\n  "
          "\t\t $$$ Price = Sqft, Length x Width of house. $$$"
          )

    print(lines)
    print(lines)
    print(lines)
    print(sp)
    return user_interface


def new_customer():
    """ This function gets the customers name and puts it into the auditor for records  and also returns customer name to main  """
    """ Function also validates for spam and if validproceeds to main  """

    new_customer_name = input("Enter Name: ")
    age = input("Enter age: ")
    auditor.append(new_customer_name)
    auditor.append(age)
    print(auditor)
    print((f"Welcome, {new_customer_name}!"))

    print("*"*78)

    if new_customer_name.isdigit():
        print("ERROR: Pleas try again, Enter Name")
    else:
        print(f"{new_customer_name},")

        while new_customer_name.isdigit() != True:
            print("We offer Several packages...\n")
            sleep(.5)

            print("1. Inside Cleaning ---------------------->",
                  total_services['Regular'], "\t\t$100.00")
            sleep(.5)
            print("2. Inside Premium  ------------->",
                  total_services['Premium'], "\t\t$200.00")
            sleep(.5)
            print("3. Outdoor Services --------------------->",
                  total_services["Outdoor"], "\t$300.00")
            print("Additional $", price_per_square_foot.__round__(2),
                  " per square foot of house is charged.")
            sleep(.5)
            print(" ")
            break

        sleep(1.5)
        print(" ")
        sleep(1.5)
        return new_customer_name, auditor, age


def show_offering(total_services):

    lines = "-"*80
    for total_service in total_services:
        print(total_service, total_services["Regular"],total_services["Premium"],total_services["Outdoor"])
        print(lines)
        return

        sleep(0.5)


def customer_transaction():
    """ This function will determine what the customer whats as a service and then gather the details which lead to payment """

    sleep(1)
    service_selection = int(input(
        "\nPrepare for selection:\nPress ----- [1] ----------> Regular\nPress ----- [2] ----------> Premium\nPress ----- [3] ----------> Outdoor\n"))

    if service_selection == int(1):
        # service_selection = regular
        print(f"You chose:\n {total_services['Regular']}")
        service_selection = total_services['Regular']

    elif service_selection == int(2):
        print(f"You chose:\n {total_services['Premium']}")
        service_selection = total_services['Premium']

    elif service_selection == int(3):
        print(f"You chose:\n {total_services['Outdoor']}")
        service_selection = total_services['Outdoor']

    else:

        if service_selection != total_services['Regular'] or total_services['Premium'] or total_services['Outdoor']:

            print("You must make a selection")
            print("Enter 1 2 or 3 ")
            customer_transaction()
    auditor.append(service_selection)
    print("\nNext: measure length and width exterior\n".center(40))
    return service_selection, auditor


def area_of_house():

    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    area = l * w
    print(f"Area = {area}")
    total_price = price_per_square_foot * area
    print(f"Total price = {total_price}")


def measurments(l, w):
    """This function asks for the values of house size used to compute the prices"""
    square_footage = int(l) * int(w)
    a = input(
        "Enter Length for side of house for example\n ' 30 ' if side is 30feet".center(50))
    b = input(
        "Enter Width for side of house for example\n '20' if side is 20 feet".center(50))
    return square_footage, a, b


def print_final_message(service_selection, service_price, total_price):
    """ This function is the professors function.
    """
    # This is the professors code , the one code snippet that I used
    print("\t\tThank you for choosing---> ", service_selection)
    print("\t\tTotal amount due for services--->", service_price)
    print("\t\tFinal total--->", total_price)


def main():
    my_greeting()
    user_interface()
    customer_age = new_customer()

    user_interface()

    show_offering(total_services)

    customer_transaction()
    new_customer_name = area_of_house()



main()
