""" Still Work to be done """
from time import sleep
import colorama
from colorama import Fore, Style


auditor = []
price_per_square_foot = float(5.00)
regular = [
    "General Tidying",
    "Sweep",
    "Dust",
    "Mop",

]
premium = [
    "Regular Services + ",
    "Bathrooms",
    "Closets",
    "Discount",
    "Senior Discount",


]
outdoor = [
    "Mowing ",
    "Pruning",
    "WeedWhacking",
    "Pressure Wash",
]

total_services = [
    ["regular:", "General Tidying", "Sweeo", "Dust", "Mop"],
    ["Premium:", "Regular Service + ", "Bathroom", "Closet", "Senior Discount"],
    ["Outdoor:", "Mowing", "Pruning", "WeedWhacking", "Senior Discount"],
]


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
    print(regular.center(80), end='')
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
    auditor.append(new_customer_name)
    print(auditor)
    print((f"Welcome, {new_customer_name}!"))

    print("*"*78)

    if new_customer_name.isdigit():
        print("ERROR: Pleas try again, Enter Name")
    else:
        print(f"{new_customer_name},")

        while new_customer_name.isdigit() != True:
            print("We offer Several packages...")
            sleep(.5)

            print("Inside Regular Cleaning -------->", regular)
            sleep(.5)
            print("Inside Delux Clearning --------->", premium)
            sleep(.5)
            print("Outdoor Services --------------->", outdoor)
            sleep(.5)
            print(" ")
            break
        print("*Prepare for selection ".center(24))
        sleep(1.5)
        print(" ")
        sleep(1.5)
        return new_customer_name, auditor


def show_offering(total_services):

    menu_lines = colorama.ansi
    for total_services in regular, premium, outdoor:
        print(total_services)
        print(menu_lines)
        sleep(0.5)


def customer_transaction():
    """ This function will determine what the customer whats as a service and then gather the details which lead to payment """

    selection_auditor = []
    sleep(1)
    service_selection = int(input(
        "Prepare for selection:\nPress ----- [1] ----------> Regular\nPress ----- [2] ----------> Premium\nPress ----- [3] ----------> Outdoor\n"))

    if service_selection == 1:
        # service_selection = regular
        print(f"You chose  {regular}")
        service_selection = regular

    elif service_selection is 2:
        print(f"You chose {premium}")
        service_selection = premium
    elif service_selection == 3:
        print(f"You chose {outdoor}")
        service_selection = outdoor

    else:

        if service_selection != int(1) or int(2) or int(3):

            print("You must make a selection")
            print("Enter 1 2 or 3 ")
            customer_transaction()
    auditor.append(service_selection)
    print("Get ready for price".center(40))
    return service_selection, auditor


def area_of_house():

    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    area = l * w
    print(f"Area = {area}")
    total_price = price_per_square_foot * area
    print(f"Toal prce = {total_price}")


def getter(get_price):
    des = {
        1: "250.00",
    }
    get_price = input("")


def measurments(l, w):
    """This function asks for the values of house size used to compute the prices"""
    square_footage = int(l) * int(w)
    a = input(
        "Enter Length for side of house for example\n ' 30 ' if side is 30feet".center(50))
    b = input(
        "Enter Width for side of house for example\n '20' if side is 20 feet".center(50))
    return square_footage, a, b


def print_final_message(service_type, service_price, total_price):
    """ This function is the professors function.
    """
    # This is the professors code , the one code snippet that I used
    print("\t\tThank you for choosing---> ", service_type)
    print("\t\tTotal amount due for services--->", service_price)
    print("\t\tFinal total--->", total_price)


def main():
    data = auditor
    my_greeting()
    user_interface()
    new_customer()
    show_offering(total_services)

    customer_transaction()
    new_customer_name = area_of_house()

   # print_final_message(service_selection, total_services, total_price
main()
