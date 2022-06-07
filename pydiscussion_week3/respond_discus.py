def main():

    #Prompt user for their name
    name=input("What is your name? ")
    
    #Display a welcome message
    print("Hello", name, "welcome to your Enlisted Advancement Sheet!")
    print("\n")
    print("Let us determine if you have been selected for advancement this promotion cycle!")
    
    #Prompt user for their exam raw score
    rawScore= int(input("Please enter the score you received on your advancement exam: "))

    #Prompt user for the amount of awards points they have
    awards= int(input("Please enter the amount of award points you have (if any): "))

    #Prompt user for the amount of PNA (passed not advanced) points that carried over from last exam cycle
    PNA= int(input("Please enter the amount of PNA points you have (max of 8): "))
    
    #Calculate the total amount of points they have 
    totalScore = rawScore + awards +PNA
    
    print("Your total score was", totalScore)
    print("\n")
    #Pass Exam AND Selected
    if (totalScore>=188):
        print("CONGRATULATIONS!",name, "You have passed the advancement exam with a score of", totalScore)
        print("\n")
        print("You have been selected for advancement to the next pay grade!")
        print("\n")
        print("Thank you for visiting the Enlisted Advancement Sheet", name, "I wish you")
        print("the best in life and have a great day!")

    #Pass, but not selected
    elif(totalScore>=150 and totalScore<188):
        print("Unfortunately", name, "you have passed the advancement exam with a score of", totalScore)
        print("but were not selected for advancement, as the minimum score to advance was 188")
        print("\n")
        print("However, you will carry 8 points over to your next advancement exam for passing the exam")
        print("\n")
        print("Thank you for visiting the Enlisted Advancement Sheet", name, "I wish you")
        print("the best in life and have a great day!")
        print("\n")
    #Fail Exam
    else:
        print("Unfortunately",name, "you have not passed the advancement exam with a score of", totalScore)
        print("as the minimum score to pass the advancement exam was 150")
        print("\n")
        print("Therefore, you are not eligible for advancement")

    #Out
        print("\n")
        print("Thank you for visiting the Enlisted Advancement Sheet", name, "I wish you")
        print("the best in life and have a great day!")



main()

    
    

print('-------------------------------------------editedcodebelow------------------------------------------------')
#My Code is Below print statement, I wanted List the branches and say 
#Thank you for joing Americas military 
branches_of_military = ['Army: Soldiers', #I want to list all the Branches and 
#Write a thank you
                        'Air_force: Airmen',
                        'Navy: Seamen',
                        'Marines: Marines',
                        'Space_force: ...'
                        ]
for a in branches_of_military:
    print(a)
print("Thank you for serving in America's Military!")
print('----------------------------------------editedcodeabove---------------------------------------------------')
