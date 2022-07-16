delux_indoor_price = 150
reg_indoor_price = 75
outdoor_package = 100


def my_greeting():
    """This program will present a customer with a business model.
        
        The customer(user) will have the opportunity to chooose
        between several different Clearning Packages. 
        The the user will select the package by entering a number,
        for example, 5 = General cleaning package, then computations 
        will run and provide the user with the total price of their selections
         \nUsing a for statement to prompt my class greeting message
    
    
    """

    my_name, my_date, my_class = "Jason Preneveau", "9 July 2022", "CMIS-120\n\n\n"
    for _ in my_name, my_date, my_class:  # '_' is a throw away variable, The compiler will use it once and forget
        # about _, likee placeholder
        opening_hint = "*** Please adjust screen to wide for best picture ***\n\n\n"

        print(_)
    print(opening_hint.center(80))


def user_interface():
    """ This function is the customer display model"""
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
        " \t\tGeneral Tidying  \t\tIncludes Bed / Bath +\n\t\t\t  \t\t\tClosets\n\t\t\t  \n\t\t\t   \t\t\t*1/2 Price Next Visit")
    print(" \t\t")
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
          "\t\t *** $200.00 if combined with inside cleaning ***")

    print(lines)
    print(lines)
    print(lines)
    print(sp)
    return (user_interface)


def user_name():
    valid_name = False
    provider = input("Please Enter your name, hit enter when done: ")

    if provider == range(0, 9):

        print("Invaid Entry, hit enter to continure...")
    else:
        valid_name = True
    return provider, valid_name


def print_final_message(service_type, service_price, total_price):
    print("\t\tThank you for choosing---> ", service_type)
    print("\t\tTotal amount due for services--->", service_price, )
    print("\t\tFinal total--->", total_price)

    return (service_price, service_price, total_price)


indoor_regular = [
    "Dust",
    "Sweep",
    "Vacuum",
    "General Tidying",
    "Senior Discount",
    float(100.00)

]

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


def main():
    my_greeting()
    user_interface()
    user_name()
    get_final_message()


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
