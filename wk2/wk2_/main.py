

ui_spaces = " "
corp = "Welcome to Paper Boy 85"
corp_center = corp.center(55)
ui = "="*60
title = "This program will describe a small paper boy route and then prompt the to bethe paper boy"

print(title)
print(ui_spaces)
print(corp_center)
print(ui)
print('{:<15}{:^20}{:<20}'.format("PRICE PER PAPER","WEEKLY SALARY","COMMISSION"))
print(ui_spaces)
print('{:<10}{:^22}{:>7}'.format("1.00$","10.00$",".25$"))
print(ui,'\n')



print("\n\nok")

def my_scripts(args):
    result = []
    result.append(args)
    return result


