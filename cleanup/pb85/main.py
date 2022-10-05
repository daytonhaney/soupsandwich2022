# def program_intro():
ui_spaces = " " # ui = user interface
corp = "[This program will describe the pay for paperBoy 85]"
paper_boy = "Welcome To PaperBoy '85\n"
paper_boy_center = paper_boy.center(70)
corp_center = corp.center(20)
ui = "=" * 80

print(ui_spaces)
print(corp_center)
print(paper_boy_center)

# vars in the global scope 
data = []
part_salary = int(10)
full_salary = int(20)
commission = float(0.25)
part_t = "Part Time"
full_t = "Full Time"
    
print(ui_spaces)
print(ui)
print('{:<13}{:^20}{:^20}{:>10}'.format("PRICE PER PAPER","COMMISSION","FT WEEKLY SALARY","PT WEEKLY SALARY"))
print(ui_spaces)
print('{:<10}{:^22}{:>15}{:>20}'.format("1.00$","$0.25","$100.00","$50.00")) 
print(ui, '\n')
# return program_intro
def your_schedule():
    prompt_ForP = input("Are you full time or part time?\n")

    if (prompt_ForP == "part time" or "Part time" or "PART TIME" or "Part Time"): #if not full time then part time 
        print(f"----------> {prompt_ForP} \n")
        print(f"{prompt_ForP} is 10 hours per week, Goal: 150 news-papers \n")
        data.append(prompt_ForP)
        page_pauser = input("Press ENTER to continue: \n")
        amount_delivered = int(input("Number of news-papers delivered: "))
        total_commission = amount_delivered * commission
        big_total = part_salary + total_commission
        round_big_total = round(big_total,2)
        print(total_commission, f" is your commission, with {part_salary} your total salary \n")
        print(round(total_commission + part_salary,2), "is your total cash take home for week ")
    else:
        (prompt_ForP == "full time" or "Full time" or "FULL TIME" or "Full Time") # full time here 
        print("----------> ")
        print(f"{prompt_ForP} is 20 hours per week, Goal: 100 news-papers \n")
        data.append(prompt_ForP)
        page_pauser = input("Press ENTER to continue: \n")
        amount_delivered = int(input("Number of news-papers delivered? ------->  \n"))
        total_commission = amount_delivered * commission
        big_total = full_salary + total_commission
        round_big_total = round(big_total,2)
        print(total_commission, f" is your commission, with {full_salary} your total salary \n" )
              
def main():
    your_schedule()
main()    # ..tbc  
