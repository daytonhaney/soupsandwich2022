
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
















#while question != exit:


#    print(question)
        
    
    
        
