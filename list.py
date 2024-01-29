from datetime import datetime
from time import sleep

import pyfiglet

auditor = list()
price_per_square_foot = 0.5

total_services = {
    "Regular": "General-Tidying\nSweep\nDust\nMop\n",
    "Premium": "Regular-Services +\nBathroom\nClosets\nLaundry\n",
    "Outdoor": "Mowing\nPruning\nWeedWhacking\nSenior-Discount\n",
}


def greeter(customer_name: str, dt: str):
    dt = datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    for _ in customer_name, dt:
        auditor.append(customer_name)
        print(customer_name, dt)
        return customer_name, dt


def user_interface():
    """This function is the customer display model"""
    sp = ""
    lines = "=" * 78

    # Line 18 to approx line 40 is code from previous weeks, put on wide view for best views
    print(lines)
    print(lines)
    # trying to maintain P#P8 Standard 78 characters
    print("=" * 22, "**Welcome to In & Out Services**", "=" * 22)
    print(lines)
    print(lines)

    regular = "Regular Service - Premium Service - Outdoor Service \n\n"

    print("")
    print(regular.center(80), end="")
    print(sp)  # old code but I like how it looks
    print("\t\tRegular Services:  \t\tPremium Services:")
    print(
        " \t\t -General Tidying  \t\t -Includes Bed / Bath +\n\t\t -Dust Mop Sweep  \t\t -Closets\t\t\t  \n\t\t\t   \t\t\t -1/2 Price Next Visit"
    )
    print(sp)
    print(sp)
    print(
        "\t\tOutdoor "  # qqqqq
        "Services "
        "Include: \n"
        "\t\t-Mowing \n"
        "\t\t-Pruning \n"
        "\t\t-Weed-Wacking \n"
        "\t\t-Pressure Wash \n"
        "\t\t-$100.00 \n\n  "
        "\t\t round: Price = Sqft, Length x Width of house. $$$"
    )

    print(lines)
    print(lines)
    print(lines)
    print(sp)
    return user_interface


def service_selection(selection):
    total_services["Regular"] == int(1)
    total_services["Premium"] == int(2)
    total_services["Outdoor"] == int(3)
    selection = int(
        input(
            "Press 1 for Regular Service\nPress 2 for Premium Service\nPress 3 for Outdoor Service\n"
        )
    )
    if selection == int(1):
        selection = total_services["Regular"]
        print(f"You chose\n{selection}")
    elif selection == 2:
        selection = total_services["Premium"]
        print(f"You chose\n{selection}")
    elif selection == 3:
        selection = total_services["Outdoor"]
        print("You chose\n{selection}")
    else:
        if selection != 1 or selection != 2 or selection != 3:
            print("You must make a selection")
            print("Please enter 1 2 or 3")
            service_selection(selection)
    auditor.append(selection)
    # print(f"You choose {selection}")
    return selection, auditor


def areaofhouse(l, w):
    l = int(input("Enter length of house: "))
    w = int(input("Enter width of house: "))
    area: float = l * w
    print(f"Area = {area}")
    total_price = price_per_square_foot * area
    total_price = round(total_price, 2)
    print(total_price)
    return area


def main():
    yourname = input("Name: ")
    greeter(f"Welcome, {yourname}\nDate: ", " \ndt\n")
    user_interface()

    selection = service_selection(1)
    area = areaofhouse("l", "w")


if __name__ == "__main__":
    main()
