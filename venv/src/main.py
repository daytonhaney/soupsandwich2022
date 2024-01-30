#!/usr/bin/env python3
from datetime import datetime
import os
import pyfiglet
from db.db_functions import *

from time import sleep
import sqlite3

# connection and first table tested Ok
# creates sql db in current directory (DB)
#

db_created = dict()
list_audit = list()
employee_audit = dict()
cust_audit = dict()

total_services = {
    "Regular": "\nGeneral-Tidying\n Sweep\n Dust\n Mop\n $100.00\n",
    "Premium": "\nRegular Service\n Bathrooms\n Closets\n Laundry\n Senior 10% Discount\n $200.00\n",
    "Outdoor": "\nMowing\n Weed-Wack\n Shrubs\n Leaves\n Senior 10% Discount\n $200.00",
}


def banner():
    "used for ui"
    b = "=" * 78
    print(b)


def intro():
    "prints info to screen"
    inout = pyfiglet.figlet_format(" IN & OUT Cleaning Corp.")
    name, date, my_class = (
        "Jay Pren",
        datetime.now().strftime("%A, %d, %B %Y %I:%M%p"),
        "CMIS-120\n\n\n",
    )
    for i in (name, date, my_class):
        print("")
        print(i)
    employee_audit["name"] = name
    employee_audit["date"] = date
    employee_audit["class"] = my_class
    print(employee_audit)
    banner()
    banner()
    print(inout.center(78))


def user_interface():
    "ui"
    intro()
    # banner()
    # print("=" * 22, "** In & Out Services **", "=" * 30)
    # banner()
    print("")
    for display1 in [
        ["Regular:", "Premium:", "Outdoor:"],
        ["Room Clean", "Regular +", "Mow"],
    ]:
        print("\n{:>15}{:>15}{:>15}".format(*display1))

    for display2 in [
        ["Dust", "Bathrooms", "Weed-Wack"],
        ["Sweep", "Closets", "Shrubs"],
    ]:
        print("{:>15}{:>15}{:>15}".format(*display2))

    for display3 in [
        ["Mop", "Laundry", "Leaves"],
        ["$100.00", "$200.00", "$300.00"],
    ]:
        print("{:>15}{:>15}{:>15}".format(*display3))

    sleep(1)

    discount = "Age 65+ 10% Discount"
    discount_center = discount.center(50)
    print("\n", discount_center)
    banner()
    banner()
    return user_interface


def new_customer():
    valid_name = False
    addr = ""
    new_cx = input("Name:\t")
    new_age = input("Age:\t")
    addr = input("Address:\t")

    if new_cx.isdigit() is True:
        print("error, letters only")
        new_cx = input("Name:\t")
        valid_name = True

    if new_age.isalpha() is True:
        print("error, numbers only")
        new_age = input("Age:\t")

    valid_cx = new_cx.replace(" ", "") and new_cx.upper()
    valid_addr = addr.replace(" ", "") and addr.upper()
    valid_age = new_age.replace(" ", "")

    cust_audit["name"] = valid_cx
    cust_audit["age"] = valid_age
    cust_audit["address"] = valid_addr

    valid_name = True
    print("")
    print(f"Welcome, {valid_cx}")

    while valid_name == True:
        print("\n Cleaning packages...\n ")
        sleep(0.50)
        print("\n1.\n Regular Package ---> $100.00\n", total_services["Regular"], "")
        sleep(0.50)
        print("\n2.\n Premium Package ---> $200.00\n", total_services["Premium"], "")
        sleep(0.50)
        print("\n3.\n Outdoor Package ---> $300.00\n", total_services["Outdoor"], "")
        print("Additional $.15 per square foot of house is charged for labor")
        break

    print(cust_audit)

    return new_cx, new_age, addr, valid_name


def customer_transaction():
    "1 2 or 3"
    print("Chose cleaning package...")
    sleep(0.4)
    service_selection = int(
        input(
            """
    Press ---[1]---> Regular\n 
    Press ---[2]---> Premium\n
    Press ---[3]---> Outdoor\n
    """
        )
    )
    if service_selection == int(1):
        print(f"You chose:\n {total_services['Regular']}")
        service_selection = total_services["Regular"]
        cust_audit["order"] = service_selection

    elif service_selection == int(2):
        print(f"You chose:\n {total_services['Premium']}")
        service_selection = total_services["Premium"]
        cust_audit["order"] = service_selection

    elif service_selection == int(3):
        print(f"You chose:\n {total_services['Outdoor']}")
        service_selection = total_services["Outdoor"]
    else:
        if (
            service_selection != total_services["Regular"]
            or total_services["Premium"]
            or total_services["Outdoor"]
        ):
            print("Error")
            print("Enter 1 2 or 3")
            customer_transaction()
    insert_customer(
        cust_audit["name"], cust_audit["age"], cust_audit["address"], service_selection
    )


def main():
    "main fn"
    create = input("Create DB?(y/n) \t ")
    if create == str("Y"):
        con = None
        try:
            con = sqlite3.connect(DB)
            customers_table(con, cx_table_create)
            close_connection()
        except Error as e:
            print(f"{e}")

        db_created["create"] = True
        print(f"DB created {con}")

    elif create == str("N"):
        print("DB not created")
        db_created["create"] = False

    user_interface()
    new_customer()
    customer_transaction()

    print("--endmain--")


main()
