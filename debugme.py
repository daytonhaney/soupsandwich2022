""" Still Work to be done """
from time import sleep


auditor = []
price_per_square_foot = float(2.00)
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
    "Mowing",
    "Pruning",
    "WeedWhacking",
    "Pressure Wash",
]


total_services = {
    "regular": ["General tidying", "Sweep", "Dust", "Mop"],
    "premuim": ["Regular Service", "Bathroom", "Closets", "Discount", "Senior Discount"],
    "outdoor": ["Mowing", "Pruning", "Weed-Whacking", "Senior-Discount"]

}


def my_greeting():
    """This prgram will present a customer with a business model.

        The customer(user) will have the opportunity to chooose
        between several different Cleaning Packages.
sJ

    """
    my_name, my_date, my_class = "Jason Pr*&%785au", "9 July 2022", "CMIS-120\n\n\n"
    for _ in my_name, my_date, my_class:  # '_' is a throw away variable, The compiler will use it once and forget
        # about _, like placeholder
        opening_hint = "*** Please adjust screen to wide for best picture ***\n\n\n"

        print(_)
    print(opening_hint.center(80))


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

    regular = "Cleaning: Regular Services and Premium Services offered: \n\n"

    print('')
    print(regular.center(80))
    print(sp)  # old code but I like how it looks
    print("\t\tRegular  \t\t\tPremium")
    print(" \t\tGeneral Tidying  \t\tIncludes Bed / Bath +\n\t\t Dust Mop Sweep  \t\t\tClosets\n\t\t\t  \n\t\t\t   \t\t\t*1/2 Price Next Visit")
    print(sp)
    print(sp)
    print("\t\tOutdoor "  # qqqqq
          "Services "
          "Include: \n"
          "\t\t-Mowing \n"
          "\t\t-Pruning \n"
          "\t\t-Weed-Wacking \n"
          "\t\t-Pressure Wash \n"
          "\t\t-$100.00 \n"
          "\t\t *** $200.00 if combined with inside cleaning ***\n\n\n\n"
          "\t\t $$$ Price = Sqft, Length x Width of house. $$$ ")

    print(lines)
    print(lines)
    print(lines)
    print(sp)
    return (user_interface)


def new_customer():
    """ This function gets the customers name and puts it into the auditor for records  and also returns customer name to main  """
    """ Function also validates for spam and if valid, proceeds to main  """
    auditor = []

    new_customer_name = input("Enter Name: ")
    auditor.append(new_customer_name)
    print(auditor)
    print((f"\nWelcome, {new_customer_name}!"))

    print("*"*78)
    if new_customer_name.isdigit():
        print("ERROR: Pleas try again, Enter Name")
    else:
        print(f"{new_customer_name},")
        validator = True
        while validator and new_customer_name.isdigit() == True:
            print("--We offer Several packages...")
            sleep(1.5)

            print("--Inside Regular Cleaning...", regular)
            sleep(1.5)
            print("--Inside Delux Clearning..")
            sleep(1.5)
            print("--And Outdoor Services")
            sleep(1.5)
            print(" ")
        print("*Prepare for selection ".center(24))
        sleep(1.5)
        print(" ")
        sleep(1.5)
        return new_customer_name, auditor


def customer_transaction():
    """ This function will determine what the customer whats as a service and then gather the details which lead to payment """

    selection_auditor = []
    sleep(1)
    service_selection = int(input(
        "Prepare for selection:\nPress 1 --> Regular\nType 2 --> Premium\nType 3 --> Outdoor\n"))

    if service_selection == 1:
        # service_selection = regular
        print(f"You chose  {regular}")

    else:
        if service_selection == 2:
            print(f"You chose {premium}")

        else:
            if service_selection == 3:
                print(f"You chose {outdoor}")

            else:
                if service_selection != 1 or 2 or 3:
                    customer_transaction()

            print("You must make a selection")
    auditor.append(service_selection)
    print(selection_auditor, auditor)
    print("Get ready for price".center(40))
    return service_selection, auditor


def measurments(l, w):
    l = input("Enter length")
    w = input("Enter width")

    square_footage = int(l) * int(w)
    print(square_footage)
    total_price = price_per_square_foot * square_footage

    return total_price


# This function is the professors function
def print_final_message(service_selection, total_price):
    print("\t\tThank you for choosing---> ", service_selection)
    print("\t\tTotal amount due for services--->", total_price,)

    return service_selection, total_price


def main():
    auditor = []
    my_greeting()
    user_interface()

    new_customer_name = new_customer()
    customer_transaction()
    measurments(1, w)
    print_final_message()


main()
