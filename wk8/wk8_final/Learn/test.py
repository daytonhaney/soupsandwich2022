def GetName():
    # This function prompts for the customer name and validates it.
    # Input: none
    # Output: name  - customer name
    # Output: validName  - boolean flag for name valid/not valid
    # Output: addr  - customer address

    validName = False
    addr = ""   #why is this initialized?

    #Prompt for customer name
    name = input("\n\n Enter the customer name <Ent> to exit: \t ")

    #Replace spaces with NULL
    name2 = name.replace(" ","")

    #Check for ALPHA only
    if ( name2.isalpha() ):
        #convert user input "name" to Upper case
        name = name.upper()
        validName = True
        
	#Prompt for customer name
        addr = input("\n Enter the customer Addr: \t ")

    return (name, validName, addr)

GetName()
