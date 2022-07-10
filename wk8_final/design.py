


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

