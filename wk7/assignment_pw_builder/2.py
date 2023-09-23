 # checking for digits and caps 
def get_pass():
    while True:
        user_pw = input("Enter new password: ")
        if any(checker.isdigit() for checker in user_pw) and any(i.isupper() for checker in
user_pw) and len(user_pw) >= 8:
            print("Password is fine")
            break
        else:
            print("Password is not fine")
         
def main():
    get_pass()
main()
