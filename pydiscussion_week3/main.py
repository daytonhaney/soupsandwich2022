"""Jason Pr#$%@#$au
    CMIS 120
    5 June 2022
"""
print('\tWelcome to y=mx+b slope calculator\n \tEnter the values as Integers.')
# using print statements to separate code for visibility and error handling 
print('----------------------------------------------------------------------')

x=int(input('Enter an integer for x: ')) #promping the user for 3 integers 
b =int(input('Enter the y-intercept "b", another integer: ')) #
m =float(input('Enter the "m", rise over run: '))

y = m * x + b # Here is where i cheat...

def func( y = m*x+b): # the original slope formula from middle school
    return y and print(f"'You're Inputs: x={x}, m={m}, b={b}, and Slope = ",y)
   
if y >= 20:
    print('you might need a larger grid')
else:
    print('10 x 10 grid should work...') # basically the best way i can test
    # the function right now.  
    
func()

print('-----------------------Come-Back-Soon--------------------------------')
   
