def intro():
    name = "Jason Pr349567789au\n"
    date = "Summer 2022\n"
    codeclass = "CMIS-102\n"
    print(name,date,codeclass)
  #  return name,date,codeclass


ui_spaces = " "
# defining the title , a descrription of what the program does
corp = "This program will describe the pay schedule\nYou play as the paperboy determining his pay\n\n\n"
paper_boy = "Welcome to Paper Boy 85'\n"
paper_boy_center = paper_boy.center(70)
corp_center = corp.center(20) # center the title for a banner like User Interface
ui = "= " * 40

print(ui_spaces)
print(corp_center)
print(paper_boy_center)

data = []
part_salery = (10)
full_salary = (20)
commission = (.25)
partt = "Part Timer" # needed to define a string for each positions in the global scope 
fullt = "Full Timer"

print(ui_spaces)
print(ui)

print('{:<13}{:^20}{:<20} {:>10}'.format(
        "PRICE PER PAPER", "COMMISSION", "FT WEEKLY SALARY","PT WEEKLY SALARY"))
print(ui_spaces)
print('{:<10}{:^22}{:>15}{:>20}'.format("1.00$", ".25$", "20.00","10.00"))
print(ui, '\n')

# print("\n\nok")


def your_schedule():
# the control flow is built with the if, the I copied and pasted the same code into the elif, and changed the string

    prompt_for_ForP = input("Please enter your schedule, Note: Cannot be changed\n\nFull Time or Part Time? -->")

    if (prompt_for_ForP != "full time"):
        print('---')
        print(f"{prompt_for_ForP} time is 20 hrs per week, Goal: 100 news papers\n")
        data.append(prompt_for_ForP)
        page_pauser = input("...Press Enter to Continue...")
        amount_delivered = int(input("how many papers did you deliver? -->"))
        total_commission = amount_delivered * commission
        big_total = full_salary + total_commission
        round_big_total = round(big_total,2)

        print(total_commission, f"is your commission, with your {full_salary} salary, You earned ${big_total}")
        return data.append(data)

    elif (prompt_for_ForP == "full time"):
        
        print("full time is 20 hrs per week, Goal: 100 news papers\n")
        data.append(prompt_for_ForP)
        page_pauser = input("...Press Enter to Continue...")
        amount_delivered = int(input("how many papers did you deliver? -->"))
        total_commission = amount_delivered * commission
        big_total = full_salary + total_commission
        round_big_total = round(big_total,2) # a special implementation is needed to properly round elements

        print(total_commission, f"is your commission, with your {full_salary} salary, You earned ${big_total}")

        print("")
        return data.append(data)




def main():
    intro()
    
    your_schedule()
#    intro(name=Jason,date,codeclass)

main() # execution 


