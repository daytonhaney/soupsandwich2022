
from time import sleep
import datetime 
import pyfiglet
# import sqlite3


auditor = list()

total_services = {
    "Regular":"General-Tidying\n Sweep\n Dust\n Mop",
    "Premium":"Regular Service +\n Bathroom\n Closet\n Senior Discount",
    "Outdoor":"Mowing\n Pruning\n WeedWhacking\n Senior Discount"
}
 


def my_greeting():
    # about _, like placeholder
    innout = pyfiglet.figlet_format(" Welcome").center(90)

    my_name, my_date, my_class = "Jason Pr*&%785au", datetime.datetime.now(), "CMIS-120\n\n\n"
    for _ in my_name, my_date, my_class:  # '_' is a throw away variable, The compiler will use it once and forget
        # about _, like placeholder
        print(_)
    print(innout.center(90))


def banner():
    l = "="*78
    print(l)

def user_interface():
    """ This function is the customer display model"""
    sp = ''
       

    # Line 18 to approx line 40 is code from previous weeks, put on wide view for best views
    
    banner()
    banner()
    # trying to maintain P#P8 Standard 78 characters
    print("="*22, "** In & Out Services**", "="*32)
    banner()
    banner()

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

    banner()
    banner()
    banner()
    print(sp)
    return user_interface


def new_customer():
    """ This function gets the customers name and puts it into the auditor for records  and also returns customer name to main  """
    """ Function also validates for spam and if validproceeds to main  """

    new_customer_name = input("Enter Name <Enter> to exit : ")
    age = input("Enter age: ")
    auditor.append(new_customer_name)
    auditor.append(age)
    print(auditor)
    
    print((f"Welcome, {new_customer_name}!\n"))

    print("*"*78)

    if new_customer_name.isdigit():
        print("ERROR: Pleas try again, Enter Name")
    else:
        print(f"{new_customer_name},")

        while new_customer_name.isdigit() != True:
            print("\nWe offer Several packages...\n")
            sleep(.5)

            print("\n1.\n Regular Service -------------> 100.00\n",
                  total_services['Regular'], "")
            sleep(.5)
            print("\n2.\n Inside Premium  -------------> 200.00\n",
                  total_services['Premium'], "")
            sleep(.5)
            print("\n3.\n Outdoor Services ------------> 300.00\n",
                  total_services['Outdoor'], "\n")
            print(" Additional $", round(.5, 3),
                  " per square foot of house is charged.")
            sleep(.1)
            print(" ")
            break

        sleep(1.5)
        print(" ")
        return new_customer_name, auditor, age


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

            print("You must make a selection \n ")
            print("Enter 1 2 or 3 \n ")
            customer_transaction()
    auditor.append(service_selection)
    print("\nNext: measure length and width exterior\n".center(40))
    return service_selection, auditor


def area_of_house(l=0, w=0):
    area = l * w
    print(f"Area = {area}")
    total_price = 0.5 * area
    print(f"Total price = {total_price}")
    return area, total_price


def print_final_message(serviceS, service_price, total_price):

    """ This function is the professors function.
    """
    
    # This is the professors code , the one code snippet that I used
    
    serviceS = customer_transaction()
    print("\t\tThank you for choosing---> ", serviceS)
    print("\t\tTotal amount due for services--->", service_price)
    print("\t\tFinal total--->", total_price)



def main():
    my_greeting()
    user_interface()
    customer_age = new_customer()

    customer_transaction()
    l = int(input("Enter Length: "))
    w = int(input("Enter Length: "))

    area_of_house(l, w)
    prompt=int(input("Press 1 to start over:\t\t"))
    prompt = main()
    while prompt == True:
        main()
        
        while prompt != True:
            break
      
main()

