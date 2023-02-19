from time import sleep  # Rather than prompting to display the model we slowly can print the model

# Main Greeting Function Different This week, could be used as a title
def my_greeting():
    """This prgram will present a customer with a business model.
        The customer(user) will have the opportunity to chooose
        between several Cleaning Packages.
    """
    my_name, my_date, my_class = "Jason P%^%*457u", "9 July 2022", "CMIS-120\n\n\n"
    for _ in my_name, my_date, my_class:  # '_' is a throw away variable, The compiler will use it once and forget
        # about _, like placeholder
        opening_hint = "*** Please adjust screen to wide for best picture ***\n\n\n"

        print(_)
    print(opening_hint.center(80))

def user_interface():
    """ This function is the customer display model/ UI for customer Interaction which will be deployed to the Job site manager
        and the customer of job site. Customer will enter data into app and data will be sent to job site manager and HQ 
        for payment and records keeping. The app is simple, 1 or two selctions.
    """
    sp = ''
    lines = "=" * 78

    # Line 18 to approx line 40 is code from previous weeks, put on wide view for best views
    print(lines)
    print(lines)
    # trying to maintain P#P8 Standard 78 characters
    print("=" * 22, "**Welcome to In & Out Services**", "=" * 22)
    print(lines)
    print(lines)

    regular = "Cleaning: Regular Services and Premium Services offered: \n\n"

    print('')
    print(regular.center(80))
    print(sp)  # old code but I like how it looks
    print("\t\tRegular  \t\t\tDeluxe")
    print(
        "\t\tGeneral Tidying  \t\tIncludes Bed / Bath +\n\t\t Dust Mop Sweep  \t\t\tClosets\n\t\t\t  \n\t\t\t   "
        "\t\t\t*1/2 Price Next Visit")
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
    print(lines)  # more lines
    print(sp)  # and spaces
    return user_interface

def new_customer(name):
    """ Function that prints the services which are in lists and in the function we ask for the name and pass it
    through an exception making sure name  =! an integer """

    auditor = []  # storing the user name in a list call auditor
    indoor_regular_services = [  # (trying )keeping vars out of the global scope ...
        "Dusting",
        "Sweep/Mop",
        "General-Tidying",
        "Bathrooms",
    ]
    indoor_deluxe = [
        "+Regular-Services",
        "Closets",
        "Bedrooms",
        "Discount",
        "Senior-Discount",

    ]
    outdoor_services = [
        "Mowing",
        "Pruning",
        "Weed-Wack",
        "Pressure-Wash",
    ]
    try:  #
        name = input("Please Enter Name ENTER to continue: ".center(50))
        name == int(name)
    except Exception:
        name


    finally:  # if there is an error in the above code finally will keep the python runtime going to avoid crashes and system outages
        print("We Offer Several Cleaning Packages".center(50))
    sleep(1.5)  # Not much logic proved  other than for than customer readability

    print("-------> Inside Regular Cleaning".center(50))
    for _ in list(indoor_regular_services):  # using _ as the variable to print the services which are lists...
        print(_.center(50), end="\n")  # _ can be used as a throwaway variable
    sleep(1.5)
    print(" ")  # Had to add for code and program readability

    print("-------> Inside Deluxe Cleaning".center(50))
    for _ in indoor_deluxe:  # Using _ as a throw away only to print the selections
        # (indoor regular and deluxe, and outdoor services)
        print(_.center(50), end="\n")
    sleep(2)
    print(" ")

    print("-------> Outdoor Services".center(50))
    for _ in outdoor_services:
        print(_.center(50), end="\n")
    sleep(2)
    print(" ")

    print("Prepare for customer selection:".center(50))
    return name, auditor, indoor_regular_services, indoor_deluxe, outdoor_services


def getter(get_price):
    des = {
        1 :"250.00",
            }
    get_price = input("")
def measurments(l, w):
    """This function asks for the values of house size used to compute the prices"""
    square_footage = int(l) * int(w)
    a = input("Enter Length for side of house for example\n ' 30 ' if side is 30feet".center(50))
    b = input("Enter Width for side of house for example\n '20' if side is 20 feet".center(50))
    return square_footage,a,b
def print_final_message(service_type, service_price, total_price):
    """ This function is the professors function.
    """
    # This is the professors code , the one code snippet that I used 
    print("\t\tThank you for choosing---> ", service_type) # 
    print("\t\tTotal amount due for services--->", service_price)
    print("\t\tFinal total--->", total_price)

    return service_type, service_price, total_price
def main():
    my_greeting()
    user_interface()
    name, auditor, outdoor_services, indoor_regular_services, indoor_deluxe = new_customer("name")
    auditor.append(new_customer(name))
    getter(1)
    #measurments(a,b)
main()
