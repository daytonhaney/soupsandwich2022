from time import sleep 
import pyfiglet 
import datetime 

def greetings():
    name, date, address = " In And Out Cleaning\n", datetime.datetime.now(),"\n 123 Main Street"
    print(name,date,address)

def cust_name():
    Valid = False
    address = ""
    name = input("Enter name <Enter> to exit: \t ")
    name2 = name.replace("", " ")

    if (name2.isalpha()):
        name = name.upper()
        Valid = True
        address = input("\n Enter Address: \t ")
    return name, Valid, address

def get_services():
    Invalid = True 
    while(Invalid):
        services = input("What service would you like? \t ")
        if (services <0 or services > 3):
            print("\n Please enter a valid number (1-3)" )
        elif(services == 1 ):
            print("\n ... ")
        elif(services == 2 ):
            print("\n ...")
        elif (services == 3 ):
            print("\n ... ")
        else:
            Invalid = False 
        return services 


def pricegouger(services):
    Regular = 150
    Premium = 250
    Outdoor = 300 

    Tax = float(0.5)

    total_regular = Regular + Tax  
    total_premium = Premium + Tax 
    total_outdoor = Outdoor + Tax 
    return total_regular,total_outdoor, total_premium 

def banner(nameC,servicesC,RegC,PreC,OutdC):
    print("\n\n Thank you               ", nameC,end="")
    print("Total {:3d}".format(RegC))
    print("")


def cust_banner():

    RegS = 0
    Cost = 0

    lenName = len(lenName)

    while(i < lenName):
        print(custName[i],end="\t")
        print(custAddress[i], end="\t")

        ResS = RegS + PreC 






def main():
    greetings()
main()

    #mport datetime
#now = datetime.datetime.now()
#print ("Current date and time : ")
#print (now.strftime("%Y-%m-%d %H:%M:%S"))
