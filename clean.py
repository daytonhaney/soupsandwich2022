from time import sleep 
import pyfiglet 
import datetime 

def greetings():
    name, date, address = " In And Out Cleaning\n", datetime.datetime.now(),"\n 123 Main Street"
    print(name,date,address)



def main():
    greetings()
main()

    #mport datetime
#now = datetime.datetime.now()
#print ("Current date and time : ")
#print (now.strftime("%Y-%m-%d %H:%M:%S"))