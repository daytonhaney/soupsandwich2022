
def my_greeting():
    name, my_class, date = "Jason Preneveau", "CMIS-120", "6/25/2022" 
    #Everything in python starts at the 0 index 
    #All variables are passed into the {} in the format method 
    my_info_template = " Name: {0}\n Class: {1}\n Date: {2}"
    #Using string manipulation to print the class header 
    print(my_info_template.format(name,my_class,date))







def main():
    my_greeting()


main()





