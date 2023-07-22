
"""Jason Pr#$%@#$au
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
print("y = mx+ b where b is the y coordinate and x is...the x coordinates, m = slope")
print("Integers only, no floats ")
x_values = int(input("enter values for x: "))

def my_slope(x1,y1,x2,y2):
    y_values = y2-y1
    x_values = x2-x1
    m = y_values / x_values
    return m
def my_coordinates():
    x1,x2 = int(input("Enter x1: \t\t"),input("Enter x2: \t\t"))
    y1,y2 = int(input("Enter y1: \t\t"), input("Enter y2: \t\t"))
    x = (x1,x2)
    y = (y2,y1)

    


