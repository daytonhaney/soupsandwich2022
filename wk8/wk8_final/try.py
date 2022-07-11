


def WelcomeMessage():
    my_name, my_date, my_class = "Jason Preneveau\n", "9 July 2022\n", "CMIS-120"
    for x in my_name, my_date, my_class:

        print(x)
        # There are several ways to print a title that is easy to read 
        # while using vanilla python ...
        # I will use most of them in this program, two are in the WelcomeMessage()
    title = """\t\t\t\t\t  Welcome To
             \n
             \t\t\t Indoor and Outdoor Services
             \n
             """
    ctitle = title.center(35)
    
    print(ctitle)



def GetName():
    validName = False
    nm = input("\n\n Enter Name <ENTER> to exit:\t")
    name = nm.replace('' , '' )
    
    if (name.isalpha()):
        nm = nm.upper()
        validName = True
    
    return (nm,validName)







def main():
    WelcomeMessage()
    GetName()
main()




