import sys
from datetime import datetime
from time import sleep

import pyfiglet

auditor = []

total_services = {  # not exactly sure what the best data type to use is
    "Regular": "General-Tidying\n Sweep\n Dust\n Mop",
    "Premium": "Regular Service +\n Bathroom\n Closet\n Senior Discount",
    "Outdoor": "Mowing\n Pruning\n Weed-Whacking\n Senior Discount",
}


r = int(100)
p = int(200)
o = int(300)


def my_greeting():
    """tui interface message"""
    innout = pyfiglet.figlet_format(" Welcome").center(90)

    my_name, my_date, my_class = (
        "Jason Pr*&%785au",
        datetime.now().strftime("%A, %d. %B %Y %I:%M%p"),
        "CMIS-120\n\n\n",
    )
    for data in (
        my_name,
        my_date,
        my_class,
    ):
        print(data)
    print(innout.center(90))


def banner():
    """"""
    l = "=" * 78
    print(l)


def user_interface():
    """UI"""
    sp = ""

    # Line 18 to approx line 40 is code from previous weeks, put on wide view for best views

    banner()
    banner()
    # trying to maintain PEP8 Standard 78 characters
    print("=" * 22, "** In & Out Services **", "=" * 31)
    banner()
    banner()

    regular = "Regular Service - Premium Service - Outdoor Service \n\n"

    print("")
    print(regular.center(81), end="")
    print(sp)  # old code but I like how it looks
    print("\t\tRegular  \t\t\tPremium")
    print(
        " \t\t -General Tidying  \t\t -Includes Bed / Bath +\n\t\t -Dust Mop Sweep  \t\t -Closets\t\t\t  \n\t\t\t   \t\t\t -1/2 Price Next Visit"
    )
    print(sp)
    print(sp)
    print(
        "\t\tOutdoor "
        "Services "
        "Include: \n"
        "\t\t-Mowing \n"
        "\t\t-Pruning \n"
        "\t\t-Weed-Whacking \n"
        "\t\t-Pressure Wash \n"
        "\t\t-$100.00 \n\n  "
        "\t\t $$$ Price = Sqft, Length x Width of house. $$$"
    )

    banner()
    banner()
    banner()
    print(sp)
    return user_interface


def new_customer():
    """This function gathers customer info"""

    new_customer_name = input("Enter Name:  ")
    age = int(input("Enter age: "))
    # print(auditor)

    print(f"Welcome, {new_customer_name}!\n")
    banner()

    if new_customer_name.isdigit():
        print("ERROR: Pleas try again, Enter Name")
    # elif new_customer_name == input("Enter")

    else:
        print(f"{new_customer_name},")

        while new_customer_name.isdigit() != True:
            print("\nWe offer Several packages...\n")
            sleep(0.5)

            print(
                "\n1.\n Regular Service ---> $100.00\n", total_services["Regular"], ""
            )
            sleep(0.5)
            print(
                "\n2.\n Inside Premium  ---> $200.00\n", total_services["Premium"], ""
            )
            sleep(0.5)
            print(
                "\n3.\n Outdoor Services ---> $300.00\n",
                total_services["Outdoor"],
                "\n",
            )
            print("Additional $.10 per square foot of house is charged.")
            sleep(0.1)
            print(" ")
            break

        sleep(1.5)
        print(" ")
        auditor.append(new_customer_name)
        auditor.append(age)
        return auditor


def customer_transaction():
    """customer selections 1 2 or 3"""

    sleep(1)
    service_selection = int(
        input(
            "\nPrepare for selection:\nPress ----- [1] ---> Regular\nPress ----- [2] ---> Premium\nPress ----- [3] ---> Outdoor\n"
        )
    )

    if service_selection == int(1):
        # service_selection = regular
        print(f"You chose:\n {total_services['Regular']}")
        service_selection = total_services["Regular"]

    elif service_selection == int(2):
        print(f"You chose:\n {total_services['Premium']}")
        service_selection = total_services["Premium"]

    elif service_selection == int(3):
        print(f"You chose:\n {total_services['Outdoor']}")
        service_selection = total_services["Outdoor"]

    else:
        if (
            service_selection != total_services["Regular"]
            or total_services["Premium"]
            or total_services["Outdoor"]
            or service_selection == str()
        ):
            print("You must make a selection \n ")
            print("Enter 1 2 or 3 \n ")
            customer_transaction()
    auditor.append(service_selection)
    print("\nNext: measure length and width exterior\n".center(40))
    return service_selection, auditor


def area_of_house(l=0, w=0):
    "Price depends on the area of house"
    tax = float(0.05)
    l = float(input("Enter Length: (rounded to nearest 10th)"))
    w = float(input("Enter Width: (rounded to nearest 10th)"))
    ppsqft = float(0.10)  # price per square
    area = l * w
    labor_price = area * ppsqft
    total_price = labor_price + tax
    print(f"Total due:  = {total_price}")
    return area, total_price


def print_final_message(serviceS, service_price, total_price):
    """This function is the professors function."""

    # This is the professors code , the one code snippet that I used

    serviceS = customer_transaction()
    print("\t\tThank you for choosing---> ", serviceS)
    print("\t\tTotal amount due for services--->", service_price)
    print("\t\tFinal total--->", total_price)


def main():  # finish pricing
    my_greeting()
    user_interface()
    new_customer()
    customer_transaction()
    l = int(input("Enter Length: "))
    w = int(input("Enter Width: "))

    area_of_house(l=0, w=0)
    # prompt=int(input("Press 1 then Enter to start over:\t\t\nPress Enter to exit: \t\t"))
    while True:
        prompt = input("Press Enter to exit program, Press 1 to go again:\t\t")
        if prompt == "":
            print("Thanks for coming, bye.")
            sys.exit()
        else:
            prompt != int(1)
            main()


if __name__ == "__main__":
    main()
