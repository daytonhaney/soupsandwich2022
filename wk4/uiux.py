"""used this in the final program that is .......unfinished
"""



   reg_large = ('200USD')
    regular = [["Regular Services", "Bathrooms", "Trash", "Sweep/Vacuum"]]
    #premium_model = [["Premium services", "Trash", "Dust", "Closets", "Laundry", "1/2 Price next visit"]]


    print(lines)
    print(sp)
    print("="*22,"**Welcome to JPPHome Cleaners**","="*23) # trying to maintain P#P8 Standard 78 characters 
    print(lines)#
    print(lines)

    regular = str("We offer Regular Service and Premuim Service")

    print('')
    print('*'*14,regular,'*'*14)
    print(sp)
    print("\t\t[Regular]  \t\t\t[Premium]")
#print('-'*78)
    print("\t\t[Sweep/Vacuum] \t\t\t[Sweep/Vacuum]\n\t\t[Trash]  \t\t\t[Trash]\n\t\t[Bathrooms]  \t\t\t[Bathrooms]")
    print("\t\t[Dust]  \t\t\t[Dust]\n\t\t\t  \t\t\t[*Closets]\n\t\t\t  \t\t\t[*Laundry]\n\t\t\t   \t\t\t[*1/2 Price Next Visit]")
    print(sp)
    print(sp)

    print(lines)
    print('\tPrices:\tRegular \t\t\tPremium')
    print('\t\t7 + rooms =',reg_large,'\t\tAdd 50USD for Premium Services')
    print('\t\t4-6 rooms =',reg_med)
    print('\t\t4 rooms and under =',reg_small)
    print(sp)
    return ui
def offer(*selection,**regular):
    selection = input("Do you need regular of premium service? ")
    if selection == regular:
        print("Thank you for choosing reguluar service: :X")
    elif selection == 'premium':
        premium_deal = 'Half price next visit', premium_deal
    else:
        pass    
def num_room(*x,**error):
    x = int(input("Enter number of rooms:    "))
    if x <=4:
        print("ok, you have less than 4 rooms\tPrice: 200.00USD")
    elif x >=5 and x<=6:
        print("regular medium price = 150USD, Thank you for your buisness. ")
    elif x > 7:
        print("regular large price = 200USD, Thank you for your business")
    else:
        return 
    
    def reg_model(model,regular):
        if regular:
            return 'Thank youu' + model
      

#def premium_model(*x,**y):
    y = input("")
    
    x = ["closet cleaning","laundry","1/2 price vext visit"]
    


def main():
    ui()
    offer()
    num_room()
main()
