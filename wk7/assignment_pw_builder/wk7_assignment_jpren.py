caps = 'QWERTYUIOPASDFGHJKLZXCVBNM'
nocap = 'qwertyuiopasdfghjklzxcvbnm'
special = '!@#$%^&*()-_=+'
nums: int = '0987654321'
check = True
prompt = input("Enter Password: ")


def nsa_quality():
    True
    valid = prompt
    if len(valid) <= 7 and valid.isdigit() == True:
        print("Not long enough...Must be between 8 and 16")



def nsa_super_quality():
    nsa_quality()
    caps_valid = prompt
    while True:
        if caps in caps_valid:
            pass
        else:
            
            print("You need a capital letters to proceed")
            break



def is_special_in_password():
    nsa_super_quality()
    
    special_valid = prompt
    while True:
        if special in special_valid:
            pass
        else:
            print(f"You need at least one {special} and a {caps}")
            break
            
def main():
    is_special_in_password()

main()







