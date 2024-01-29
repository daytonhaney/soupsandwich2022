from datetime import datetime
from time import sleep

daily_totals = {}

auditor = {}


def cust_name():
    valid = False
    address = ""
    name = input("F <Enter> to exit: \t ")
    fname = name.replace("", " ")

    if fname.isalpha():
        fname = name.upper()
        address = input("\n Enter Address: \t ")

    while True:
        try:
            age = int(input("Age: "))
            if age >= 0 and age <= 120:
                print(age)
                return age
        except ValueError:
            print("invalid age..")
        # break
        continue

    auditor["age"] = age
    auditor["fname"] = name
    auditor["address"] = address


def pricegouger(services):
    "services"
    Regular = 150
    Premium = 250
    Outdoor = 300

    Tax = float(0.5)

    total_regular = Regular + Tax
    total_premium = Premium + Tax
    total_outdoor = Outdoor + Tax
    return total_regular, total_outdoor, total_premium


def main():
    "main"
    customer = cust_name()
    get_paid = pricegouger("getMoney")


main()


# mport datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))
