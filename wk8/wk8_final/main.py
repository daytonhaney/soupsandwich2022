# 
#
#



title = "{:<15}".format("Please adjust width to 80 for best view")
print(title)

large_house = ""

def my_greeting(): 

    my_name, my_date, my_class = "Jason Preneveau\n", "9 July 2022\n", "CMIS-120"
    for _ in my_name, my_date, my_class:

        print(_)
    title = "Welcome to In and Out Services\n"
    ctitle = title.center(80)
    from test import mow 
    print(title,mow)

def main():
    my_greeting()


main()


def Get_User_Value():
    indoor = 0 
    outdoor = 0

    user_input = []
    user_input = input("Would you need Indoor or outdoor cleaning?")
    # validate the user input with if statements 
    if user_input == "indoor":
        print("Indoor Services")
        return user_input


