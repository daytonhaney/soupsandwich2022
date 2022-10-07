# 
import pyfiglet 
# or you can turn your python into "zombie python" which is criss crossed imports all over the local 


def main():
    import pyfiglet # i read to keep your imports in the same venv file 
    
    print("-- please adjust window width if banner looks messed up")    
    my_banner = pyfiglet.figlet_format("                   welcome") # pip3 import pyfiglet is a python3 command line utility to get colors and art in the terminal, where we run our programs. 
    print(my_banner) #adjust width if Banner is messed up
      
    
    def my_introduction(name,my_class,date): #created a new greeting funcion
        print(f"{name}\n{my_class}\n{date}") # f strings come in handy 
    my_introduction("  Jason Preneveau", "  CMIS-120", "  19 June 2022") # # #since function variables are returned as strings by  defauft 
    # You can just call three strings like naae class and date
main()


_EXITLOOP = -99 #depingg on value of this variable is what allows exiting of loop   
question = int(input("Number of miles driven on Monday:\n "))

while question != _EXITLOOP:
    monday = question
    print(f"You drove {question} miles on Monday.")
    
    monday = int(input("Number of miles driven on Tuesday:\n "))
    print(f"You drove {question} miles on Tuesday.")
    
    while question != _EXITLOOP :
        tuesday = question
        tuesday = int(input("Number of miles driven on Wednesday:\n "))
        print(f"You drove {question} miles on Wednesday.")
        
        while question!=_EXITLOOP:
            wednesday = question
            wednesday = int(input("Number of miles driven on Thursday:\n "))
            print(f"You drove {question} miles on Thursday.")
            while question !=_EXITLOOP:
                thursday = question
                thursday = int(input("Number of miles driven on Friday:\n "))
                print(f"You drove {question} miles on Friday.")
                while True: # I could not ggte program to stop looping so I came up with this 
                    break
                break
            break
        break
    break
print("Thanks for commmng!") # I wanted to put the entire loop into the function but I did not have time to make the gloabl vaiables local to the function 
    



def average(my_list): # I look the input questions and put them in a list so that i could create a bas average function to fun on it  and get the average restuls 
    average = sum(my_list) / len(my_list)
    return average


my_list = [question,monday,tuesday,thursday]

avg_gas = average(my_list)
print(f"{avg_gas} Is your average miles weekly") # if you know your weekly average of miles you can easily guestimate how much you are speding on gas 


main() # 

main



