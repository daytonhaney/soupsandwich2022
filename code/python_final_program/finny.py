from ast import ExceptHandler
from time import sleep
from tokenize import Name



def my_greeting():
    """This prgram will present a customer with a business model.
        The customer(user) will have the opportunity to chooose
        between several different Cleaning Packages.
    """
    my_name, my_date, my_class = "Jason Preneveau", "9 July 2022", "CMIS-120\n\n\n"
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
    print("\t\tRegular  \t\t\tPremium")
    print(
        "\t\tGeneral Tidying  \t\tIncludes Bed / Bath +\n\t\t Dust Mop Sweep  \t\t\tClosets\n\t\t\t  \n\t\t\t   \t\t\t*1/2 Price Next Visit")
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
    print(lines) # more lines
    print(sp) # and spaces
    return user_interface

 
def new_customer(name): #trying to keep all vars out of the global scope
    """ Function also validates for spam and if valid, proceeds to main  """
    
    auditor = []
    indoor_regular_services = [  # keeping vars out of the global scope ...
        "Dusting",               # for safer code        
        "Sweep/Mop",
        "General-Tidying",
        "Bathrooms",
    ]
    indoor_delux = [
        "+Regular-Services", 
        "Closets",
        "Bedrooms",
        "Discount",
        "Senior-Discount",
        
    ]
    outdoor_services = [
        "Mowing",
        "Pruning",
        "WeedWacking",
        "Pressure-Wash",
        
    ]
    
    
    try:
        name = input("Please Enter Name:".center(50))
        name == int(name)   
    except Exception:
        print(" When ready, select by using 1 , 2 , or 3  ".center(50))
    
    finally:
        #except ValueError:
        #print("Welcome to the In and and Out Cleaners \n")

        print("--We offer Several packages...\n")
    sleep(1.5)  # Using sleep for interactvity purposes

    print("[Inside Regular Cleaning]".center(50))

    for _ in list(indoor_regular_services):
        print(_.center(50),end="\n")
    sleep(1.5)
    print(" ") # Had to add for code and program readability 
            
    print("[Inside Delux Clearning]".center(50))
            
    for _ in indoor_delux: # Using _ as a throw away only to print the selections (indoor regular and delux, and outdoor services)
        print(_.center(50),end="\n")
    sleep(1.5)
    print(" ")
    
    print("[Outdoor Services]".center(50))
    for _ in outdoor_services:
        print(_.center(50),end="\n")
    sleep(1.5)
    print(" ")
    print("Prepare for customer selection:".center(50))
    sleep(1.5)
    print(" ")
    print("last before return stmt")# debug print stmt
    return name
    


def customer_transactions():
    """This function will determine what the customer what's as a service and then gather the details which lead to\
    payment"""

    auditor = []

    auditor.append(service_order)
    return service_order, auditor

 
def measurments(l, w, ):
    """This function asks for the values of house size used to compute the prices"""
    square_footage = int(l) * int(w)
    return square_footage


def print_final_message(service_type, service_price, total_price):
    print("\t\tThank you for choosing---> ", service_type)
    print("\t\tTotal amount due for services--->", service_price, )
    print("\t\tFinal total--->", total_price)

    return (service_price, service_price, total_price)

 
def main():
    my_greeting()
    user_interface()

    

    name, auditor, outdoor_services,indoor_regular_services, indoor_delux = new_customer("name")
    auditor.append(new_customer(name))
    

    customer_transaction()


main()
