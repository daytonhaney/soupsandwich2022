
def pythonista():
    print("+-"*34) # pythonistas will die over this 
    
def m():
    # pythonista()
    y_vals = list()
    x_vals = list()
    pythonista()
    print(
    "This program assumes you have graphed a linear equation of a line and need to quickly find the slope (m)")
    exit = False
    y2 = float(input("y2: \t\t"))
    y1 = float(input("y1: \t\t"))
    pythonista() 
    delta_y = y2 - y1
    exit = True
    while exit == True:
        x2 = float(input("x2: \t\t"))
        x1 = float(input("x1: \t\t"))
        delta_x = x2 - x1
        m = delta_y - delta_x
        pythonista()
        print(f"slope = {m}")
        #print(pythonista) 
        x_vals.append([y2])
        x_vals.append([y1])
        y_vals.append([x2])
        y_vals.append([x1])
        print("y vals = ", y_vals)
        print("x vals = ", x_vals)
        pythonista()
        data = print(f"{y2}-{y1}/{x2}-{x1} = slope ={m}")
        print(data)
        return delta_y, delta_x
    

def main():
    m()
    while True:
        slope = input("Press 1 then <Enter> to run the program again \nPress <Enter> to quit:\t\t")
        
        if slope == str("1"):
            m()
        else:
            break
main()


"""
Work in progress 
Jason Pr#$%@#$au
    CMIS 120
    5 June 2022

import keyboard 

print('\tWelcome to y=mx+b slope calculator\n \tEnter the values as Integers.')
# using print statements to separate code for visibility and error handling 
print('----------------------------------------------------------------------')

def func(x1,y1):
    x1=int(input("Enter x1:\t\t "))
    #if x1 == syste
    y2=int(input("Enter y1:\t\t "))

    x2=int(input("Enter x2:\t\t\t"))
    y2=int(input("Enter y2:\t\t\t"))
    dY = y2-y1 
    dX = m(x2-x1)

    m = dY/dX 

#    m=(y-b)/x

    print(m)
    if y > 25:
        print("====")
    else:
        print("-------")
    
    print(m)# the original slope formula from middle school
    return m,y and print(f"'You're Inputs: x={x}, m={m}, b={b}, and Slope = ",y)
    # the function right now.  
    
func(4,6)

print('-----------------------Come-Back-Soon--------------------------------')
"""
