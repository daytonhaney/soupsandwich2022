def intro():
    name = "jay preneveay\n"
    date = "2 oct 2022\n" 
    code_class = "cmis120\n"
    print(name,date,code_class)

#def program_intro():
ui_spaces = " " # ui = user interface
corp = "This program will describe the pay for paperBoy 85'\n"
paper_boy = "Welcome To PaperBoy '85\n"
paper_boy_center = paper_boy.center(70)
corp_center = corp.center(20)
ui = " = " * 40

print(ui_spaces)
print(corp_center)
print(paper_boy_center)

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
print('{:<10}{:^22}{:>15}{:>20}'.format("1.00$",".25","20.00","10.00")) 
print(ui, '\n')
#return program_intro
def your_schedule():
    prompt_ForP = intput("Are you full time or part time?\n")
    if (prompt_ForP != "full time" or "Full time"): #if not full time then part time 
        print("----------> ")
        print(f"{prompt_ForP} is 10 hours a week, Goal: 50 news-papers\n")
        data.append(prompt_ForP)
        page_pauser = intput("Press Enter to Continue\n")
        amount_delivered = int(input("how many papers did you deliver ----> "))
        total_commission = amount_delivered * commission
        big_total = part_salary + total_commission
        rount_big_total = round(big_total,2)
        print(total_commission,f" is your commission, with {part_salary} your total salary\n")
    elif (prompt_ForP == "full time" or "Full time")# full time here 
        print({prompt_ForP}," ")
# .. tbc       
      