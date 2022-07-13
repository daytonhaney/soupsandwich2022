

def my_spacer(spacer):
    
    spacer = "="*50 
    print(spacer)
    

    
    
my_spacer("")
 
 

opening_hint = "Please adjust screen to wide for best picture"
print(opening_hint.center(100))

#my_spacer 

def my_greeting(): 

    my_name, my_date, my_class = "Jason Preneveau\n", "9 July 2022\n", "CMIS-120"
    for _ in my_name, my_date, my_class:

        print(_)
    title = "Welcome to In and Out Services\n"
    ctitle = title.center(80)
    
    print(title)

def main():
    my_spacer("=")    
    my_greeting()
    
main()

my_spacer

#print('{:=<20}'.format('Hello'))
li = []
sp = ''
"""creatring variables to build a user interface with
text so my project looks ok with out importing libs
"""

lines = "="*78
my_name = 'JPP Home Cleaners'

#a = str(input("Please enter type of service" '200USD'))
reg_med = ('150USD')
reg_small = ('100USD')
reg_large = ('200USD')
regular_model = [["Regular Services", "Bathrooms", "Trash", "Sweep/Vacuum"]]
premium_model = [["Premium services", "Trash", "Dust", "Closets", "Laundry", "1/2 Price next visit"]]


print(lines)
print(sp)
print("="*22,"**Welcome to JPPHome Cleaners**","="*23) # trying to maintain P#P8 Standard 78 characters 
print(lines)#
print(lines)

regular = str("We offer Regular Service and Premuim Service")
my_spacer("=")

print('')
print('*'*14,regular,'*'*14)
print(sp)
print("\t\t[Regular]  \t\t\t[Premium]")
#print('-'*78)
second = (["\t\t[Sweep/Vacuum] \t\t\t[Sweep/Vacuum]\n\t\t[Trash]  \t\t\t[Trash]\n\t\t[Bathrooms]  \t\t\t[Bathrooms]"])
print("\t\t[Dust]  \t\t\t[Dust]\n\t\t\t  \t\t\t[*Closets]\n\t\t\t  \t\t\t[*Laundry]\n\t\t\t   \t\t\t[*1/2 Price Next Visit]")
print(sp)
print(sp)

print(lines)
print('\tPrices:\tRegular \t\t\tPremium')
print('\t\t7 + rooms =',reg_large,'\t\tAdd 50USD for Premium Services')
print('\t\t4-6 rooms =',reg_med)
print('\t\t4 rooms and under =',reg_small) 
print(sp)
my_spacer(spacer=1)
name = input("Please state your name: ")
print("\t\t\t\t\t\t\tWelcome",name)
#a = str(input("Please enter type of service: ;)
 #             ("Press a for reg"))
reg_choice_prem_choice = input(f'Please Enter 1 for regular:  \n\n\tOR\n\nPress 2 for Premium: ')
#prem_choice = int(input("Press 2 for Premium:)
num_rooms =input("Please enter the number of rooms in your home : ")
#price_small = 1 + reg_small
#price_prem = 2 + reg_large



