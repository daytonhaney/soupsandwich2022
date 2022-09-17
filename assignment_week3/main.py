


def my_greeting(): 
# Somthing new and differnt to put my welcome message out there              
    my_name, my_date, my_class = "Jason Pr$&^$&8", "9 July 2022", "CMIS-120\n\n\n"           
    for _ in my_name, my_date, my_class: # '_' is a throw away variable, The compiler will use it once and forget 
    # about _, likee placeholder
        title = "Welcome to In and Out Services\n"
        ctitle = title.center(80)
        print(_)
    opening_hint = "*** Please adjust screen to wide for best picture ***\n\n\n"
    print(opening_hint.center(80))
    title = "Welcome to In and Out Services\n"
    ctitle = title.center(80)
    
    print(ctitle) 

def user_interface():
# creatring variables to build a user interface with
# text so my project looks ok with out importing libs
    sp = ''
    lines = "="*78

    print(lines)# Line 18 to approcimately line 40 is code from previous weeks, put on wide view for best views
    print(lines)
    print("="*22,"**Welcome to In & Out Services**","="*22) # trying to maintain P#P8 Standard 78 characters 
    print(lines)#
    print(lines)

    regular = "Cleaning: Regular Services and Premuim Services offered: \n\n"

    print('')
    print(regular.center(80))
    print(sp) # old code but I like how it looks 
    print("\t\tRegular  \t\t\tPremium")  
    print(" \t\tGeneral Tidying  \t\tIncludes Bed / Bath +\n\t\t\t  \t\t\tClosets\n\t\t\t  \n\t\t\t   \t\t\t*1/2 Price Next Visit")
    print(" \t\t")
    print(sp)
    print(sp)
    print("\t\tOutdoor "
          "Services "
          "Include: \n"
          "\t\t-Mowing \n"
          "\t\t-Pruning \n"
          "\t\t-WeedWacking \n"
          "\t\t-Pressure Wash \n"
          "\t\t-$100.00 \n"
          "\t\t *** $200.00 if combined with inside cleaning ***")    
    print("Lets do this".center(80))
    print(lines)
    print(lines) 
    print(lines)     
    print('\tPrices:\tRegular \t\t\tPremium')
    print(sp)


    delux_indoor_price = 150.00
    reg_indoor_price = 78
    outdoor_package = 100  


    return reg_indoor_price, delux_indoor_price, outdoor_package
  
def prompt_customer():
        valid_name = False 
        prompt_user = input(f"Please enter your name---->")
        greet_user = "Welcome,{}"







def print_final_message(service_type,service_price,total_price):
    print("\t\tThank you for choosing---> ", service_type) 
    print("\t\tTotal amount due for services--->", service_price,)
    print("\t\tFinal total--->", total_price)
    
"""
trim = "trim shrubs"
prune = 15
mow = "trim the bushes"
print('{:<13}{:^20}{:<20} {:>10}'.format("Indoor Services",
      "Outdoor Serives", "FT WEEKLY SALARY", "PT WEEKLY SALARY"))

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
  
indoor_regular = [  
        "Dust",
        "Sweep",
        
        "Vaccuum",
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
        200.00
]     


def main():
    my_greeting()
    user_interface()
   
main()


