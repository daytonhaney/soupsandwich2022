
import pyfiglet
 
def main():
    import pyfiglet
    
    print("-- please adjust window width if banner looks messed up")    
    my_banner = pyfiglet.figlet_format("                   welcome")
    print(my_banner)
      
    
    def my_introduction(name,my_class,date):
        print(f"{name}\n{my_class}\n{date}")
    my_introduction("  Jason Preneveau", "  CMIS-120", "  19 June 2022 (updated 06 Oct 2022)") 
main()

_EXITLOOP = -99  
question = int(input("Number of miles driven on Monday:\n "))

while question != _EXITLOOP:
    monday = question
    print(f"You drove {question} miles on Monday.")
    
    monday = int(input("Number of miles driven on Tuesday:\n "))
    print(f"You drove {monday} miles on Tuesday.")
    
    while question != _EXITLOOP :
        tuesday = question
        tuesday = int(input("Number of miles driven on Wednesday:\n "))
        print(f"You drove {tuesday} miles on Wednesday.")
        
        while question!=_EXITLOOP:
            wednesday = question
            wednesday = int(input("Number of miles driven on Thursday:\n "))
            print(f"You drove {wednesday} miles on Thursday.")
            while question !=_EXITLOOP:
                thursday = question
                thursday = int(input("Number of miles driven on Friday:\n "))
                print(f"You drove {thursday} miles on Friday.")
                while True: 
                    break
                break
            break
        break
    break

    
def average(my_list):
    average = sum(my_list) / len(my_list)
    return average


my_list = [question,monday,tuesday,wednesday,thursday]

avg_gas = average(my_list)
print(f"{avg_gas} Is your average number of miles this week.\n Come back soon.")








