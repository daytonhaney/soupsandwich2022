
def user_interface(template):
    # Building a user interface for customers

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
    print(" \t\tGeneral Tidying  \t\tIncludes Bed / Bath +\n\t\t\t  \t\t\tClosets\n\t\t\t  \t\t\t   \t\t\t*1/2 Price Next Visit")
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

    delux_indoor_price = 150.00
    reg_indoor_price = 78
    outdoor_package = 100

    return reg_indoor_price, delux_indoor_price, outdoor_package


user_interface("template")
