
ui_spaces = " "
corp = "Welcome to Paper Boy 85"
corp_center = corp.center(55)
ui = "= " *60
title = "This program will describe a small paper boy route and then prompt the to bethe paper boy"
data = []
part_salery = 10
full_salary = 20
commission = float(.25)
partt = "Part Timer"
fullt = "Full Timer"

print(title)
print(ui_spaces)
print(corp_center)
print(ui)
print('{:<15}{:^20}{:<20}'.format("PRICE PER PAPER" ,"WEEKLY SALARY" ,"COMMISSION"))
print(ui_spaces)
print('{:<10}{:^22}{:>7}'.format("1.00$" ,"10.00$" ,".25$"))
print(ui ,'\n')

print("\n\nok")

def your_schedule():
    #    data = []
    prompt_for_ForP = input("Please enter your schedule, Note: Cannot be changed\n\nFull Time or Part Time ?")

    if prompt_for_ForP != "full time":
        print("Part time is 20 hrs per week, Goal: 100 news papers\n")
        data.append(prompt_for_ForP)
        page_pauser = input("...Press Enter to Continue...")
        amount_delivered = int(input("how many papers did you deliver?"))
        total_commission = amount_delivered * commission
        big_total = full_salary + total_commission
        round_big_total = round(big_total,2)

        print(total_commission, f"is your commission, with your {full_salary} salary, You earned {big_total}")
        return data.append(data)

    elif prompt_for_ForP != "part time ":
        print("Part time is 10 hours per week, Goal: 50 news papers")
        data.append(prompt_for_ForP)
        return data.append(data)
















def main():
    your_schedule()

main()





