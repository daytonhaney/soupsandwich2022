__course__ = 'CMIS-120'
__name__ = 'Jason Preneveau'
__date__ = '28 June 2022'
__version__ = '1.1.2'

print('# ' + '=' * 78) # Hacking my way to some type of UI 
print('Name: ' + __name__) # 
print('Date: ' + __date__)
print('Course: ' + __course__)
print('Version: ' + __version__)


print('# ' + '=' * 78) 
caps = 'QWERTYUIOPASDFGHJKLZXCVBNM'
nocap = 'qwertyuiopasdfghjklzxcvbnm' # introducing my globals as the paramters 
special = '!@#$%^&*()-_=+' # makes coming up with functions very easy ^ 
nums: int = '0987654321'  
check = True
prompt = input("Enter Password: ")


def nsa_quality():
    True
    valid = prompt # in every function i create a local variable version of the global prompt 
    if len(valid) <= 7 and valid.isdigit() == True:
        print("Not long enough...Must be between 8 and 16")


def nsa_super_quality():
    nsa_quality() # i call the last function which already checks for if it has digits
    caps_valid = prompt
    while True:
        if caps in caps_valid: # I run the same function for digits except for specia characters.
            pass
        else:
            
            print("You need a capital letters to proceed")
            break # which 


def is_special_in_password():
    nsa_super_quality() # again i only have to call the previous function becuse the latter are already handled 
    
    special_valid = prompt
    while True:
        if special in special_valid:
            pass
        else:
            print(f"You need at least one {special} and a {caps}")
            break
            
def main():
    is_special_in_password()
        print('# ' + '=' * 78) # Hacking my way to some type of UI
main()







