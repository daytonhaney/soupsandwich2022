
title = "{:<15}".format("Please adjust width to 80 for best view")
print(title)


large_house = ""


def my_greeting():

    my_name, my_date, my_class = "Jason Preneveau\n", "9 July 2022\n", "CMIS-120"
    for x in my_name, my_date, my_class:

        print(x)
    title = "Welcome to In and Out Services\n"
    ctitle = title.center(80)
    print(ctitle)


def main():
    my_greeting()


main()
