import sleep 


def my_greeting():
    """This prgram will present a customer with a business model.

        The customer(user) will have the opportunity to chooose
        between several different Cleaning Packages.

        The the user will select the package by entering a number,

        for example, 5 = General cleaning package, then computations
        will run and provide the user with the total price of their selections
         \nUsing a for statement to prompt my class greeting message

    """
    my_name, my_date, my_class = "Jason Preneveau", "9 July 2022", "CMIS-120\n\n\n"
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
    print("\t\tOutdoor "
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
    return(user_interface)


def new_customer():
    """ This function gets the customers name and puts it into the auditor for records  and also returns customer name to main  """
    """ Function also validates for spam and if valid, proceeds to main  """
    auditor = []
    validator = False
    new_customer_name = input("Enter Name:     ")

    auditor.append(new_customer_name)

    print(f"Welcome to In and Out Cleaners, {new_customer_name}")
    if new_customer_name == isdigit:
        new_customer_name
        print("ERROR: Invalid customer name")
    elif new_customer_name == isalpha:
        print("Loading.....")
        sleep(1.99)
        validator == True



    if validator == True:

        return(new_customer_name,auditor,validator)


def customer_transaction():
    """ This function will ask what type of services the cusomer needs \t
    the function will also ask house measurments in Lengh X width , which determines the price of Services.
    """
    auditor = [] # As usual we will bring in the auditor for business records
    # We will prompt the "worker " to enter the measurments

    length = input("{:>70}".format("Enter Length:  "))
    width = input("{:>70}".format("Enter Width:  "))

    square_footage = int(length) * int(width)
    auditior = auditor.append(square_footage)
    return(length,width,square_footage,auditior)


def measurments(l,w):
    square_footage = int(l) * int(w)
    return square_footage




def print_final_message(service_type, service_price, total_price):
    print("\t\tThank you for choosing---> ", service_type)
    print("\t\tTotal amount due for services--->", service_price,)
    print("\t\tFinal total--->", total_price)

    return(service_price, service_price, total_price)


indoor_regular = [
    "Dust",
    "Sweep",
    "Vacuum",
    "General Tidying",
    "Senior Discount",
    float(100.00)

]

def main():
    auditor = []
    customer_choice = []
    customer_names = []
    customer_prices = []

    my_greeting()
    user_interface()
    sleep(1)
    new_customer()
    customer_transaction()


    indoor_delux = [
        "Regular Services + ",
        "Bathrooms",
        "Bedrooms",
        "Discount",
        "Senior Discount",
        float(200.00)


    ]
    outdoor_services = [
        "Mowing",
        "Pruning",
        "WeedWacking",
        "Pressure Wash",
        float(200.00)
    ]


main()
"""
trim = "trim shrubs"
prune = 15
mow = "trim the bushes"
print('{:<13}{:^20}{:<20} {:>10}'.format("Indoor Services",
      "Outdoor Services", "FT WEEKLY SALARY", "PT WEEKLY SALARY"))

print('{:<10}{:^22}{:>15}{:>20}'.format("1.00$", ".25$", "20.00", "10.00"))
#print(ui, '\n')
x = '{:<10}{:^22}{:>15}{:>20}'.format("1.00$", ".25$", "20.00", "10.00")
print(x)
print(x[:])
b = "{}"
ask = []
d = [[3], 1, 2.2]
e = ""
print(d)
  
  """

