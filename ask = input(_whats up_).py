
# This program will calculate and display the cost of purchasing a set of tires for each customer.
# The user will be prompted for how many tires to purchase. 
# The program will validate the user input.
# The progam will collect all the customer info and display it at the end.
# The progam will accumulate and display Store Totals ( sum of all customers).

# Developer: Faculty CMIS102   Date: Jan 31, 2014
# Modified: BLB	- modified for Validation	Jun 4, 2017	
# Modified: BLB	- modified for Functions	Jun 22, 2017	
# Modified: BLB	- modified for Loops		Jul 2, 2017
# Modified: BLB	- modified for Customer Name	Jul 12, 2017
# Modified: BLB	- modified for Arrays		Jul 22, 2017

# Define Functions -----------------------------------------------------------------------------------------

# Welcome ------------------------------
def Welcome():
    # This function displays the Welcome message
    print("\nWelcome to Bernie's Tire service program")
    print("\nThis program will calculate the cost of your tire purchase , including installation")

# GetName ------------------------ BLB	- added Loop for name requirement		Jul 12, 2017
#                                  BLB	- added customer address requirement	Jul 22, 2017
def GetName ():
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

# GetNumTires ------------------------
def GetNumTires ():
    # Modified: BLB	- added Loop for validation		Jul 2, 2017
    # This function prompts for the number of tires and validates between 0 and 99
    # Input: none
    # Output: numTires

    Invalid = True
	
    # Validate input 
    while (Invalid):
        #Prompt/Get user response user for number of tires
        numTires = int(input("\n\n How many tires would you like to purchase (1-99) ? "))

        # Display error msg
        if (numTires < 0):
            print("\n Please enter a positive number (1-99): ")
        elif (numTires > 99):
            print("\n *** Sorry, not that many tires are available ")
        else:
            Invalid = False
       
    return numTires


# CalCustCost ------------------------
def CalCustCost (numTires):
    # This function calculates the total cost per customer
    # Input:  numTires  - number of tires purchased
    # Output: tireCost, installCost, totalCost - total customer cost (tires + install)                


    tirePrice = 140.0	# Notice that I'm assigning these values to variables
    installPrice = 5	# These variables will be used in the calculations.

    #Calculate the cost of tires
    tireCost = tirePrice * numTires

    #Calculate the cost if installation
    installCost = installPrice * numTires

    #Calcuate the total cost 
    totalCost = tireCost + installCost

    return(tireCost,installCost,totalCost)


# DisplayOutput ------------------------
def DisplayCustOutput (nameC, numCTires, tireCCost,installCCost,totalCCost):
    # This function displays the number of tires purchased and the total cost
    # Input: numCTires  - number of tires purchased
    #        tireCCost - tire purchase cost        
    #        installCCost - install purchase cost        
    #        totalCCost - total purchase cost        
    # Output: none

    print("\n\n *** Thank you                           ", nameC,end="")
    print("  for your purchase !")
    print(" *** The number of tires purchased:       {:3d} ".format(numCTires))
    print(" *** The cost of tires purchased:       ${:7.2f}".format(tireCCost))
    print(" *** The installation cost:             ${:7.2f}".format(installCCost))
    print("\n *** The total cost of your purchase:   ${:7.2f}".format(totalCCost))


# DisplayStoreOutput ------------------------ # Added: BLB	- added for store requirements		Jul 2, 2017
def DisplayStoreOutput (numSTires, totalSCost):
    # This function displays the number of tires purchased and the total cost
    # Input: numSTires  - number of tires purchased
    #        totalSCost - total purchase cost        
    # Output: none

    print("\n\n *** Store totals for today")
    print(" *** The total number of tires purchased:  ", numSTires)
    print(" *** The total sales for the tires including installation: $", totalSCost)

# DisplayCustStoreTotals ------------------------
def DisplayCustStoreTotals (custNames, custAddrs, custTires, custCosts):
    # This function first displays all the customer info
    # and then displays the store totals (no. of tires purchased and the total sales)
    # Input: arrays
    #       custNames
    #       custAddrs
    #       custTires
    #       custCosts     
    # Output: Display


    numSTires = 0
    totalSCost = 0
    
    lenCust = len(custNames)
    print("no. of customers =",lenCust)
    i = 0
    
    print("\n========================================")
    print("Customer Info...")
    print("Name\tAddress\tNumTires\tCost")
    while (i < lenCust):
        print(custNames[i],end="\t")
        print(custAddrs[i],end="\t")
        print(custTires[i],end="\t")
        print(custCosts[i])
        
        numSTires = numSTires + custTires[i]
        totalSCost = totalSCost + custCosts[i]
        i = i + 1

        print("\n\n *** Store totals for today")
        print(" *** The total number of tires purchased:  ", numSTires)
        print(" *** The total sales for the tires including installation: $", totalSCost)
	
        print("\n *** REFORMATTED OUTPUT -------------------- ***")
	
        print('{:<20}\t{:<20}\t{:<10}\t{:<10} '.format('Name','Address','No. Tires','Total Cost'))
        print('{:<20}\t{:<20}\t{:<10}\t{:<10} '.format('____________________','____________________','__________','__________'))
    i = 0
    while (i < lenCust):
        print('{:<20}\t{:<20}\t{:10d}\t{:10.2f} '.format(custNames[i], custAddrs[i], custTires[i], custCosts[i]))
        i = i + 1

    storeID = 'StoreID: 3406'
    print('{:<20}\t{:<20}\t{:<10}\t{:<10} '.format('____________________','____________________','__________','__________'))
    print('{:<20}\t{:<20}\t{:10d}\t{:10.2f} '.format(storeID, 'Store totals:', numSTires, totalSCost))


#Main ---------------------------------------------------------------
def main():
	numTiresStore = 0
	totalCostStore = 0
	moreCustomers = True
	custName = None
	custAddr = None
	
	custNames = list()
	custAddrs = list()
	custTires = list()
	custCosts = list()

	# Display Welcome message
	Welcome()

	while (moreCustomers):
		
		#Prompt user for customer name - # Added: BLB	- added for name requirements		Jul 12, 2017 
		custName,validName,custAddr = GetName()    
		moreCustomers = validName

		if (validName):
			#Populate arrays
			custNames.append(custName)
			custAddrs.append(custAddr)

			#Prompt user for number of tires 
			numTires = GetNumTires()
			custTires.append(numTires)

			#Calculate the customer cost
			tireCost,installCost,totalCost = CalCustCost (numTires)
			custCosts.append(totalCost)

			#Diplay output (optional)
			DisplayCustOutput (custName, numTires, tireCost,installCost,totalCost)

			# Accumulate store totals - # Added: BLB	- added for store requirements		Jul 2, 2017
			#numTiresStore = numTiresStore + numTires	- removed- added to DisplayCustStoreTotal		Jul 22, 2017
			#totalCostStore = totalCostStore + totalCost


	#Display Store totals output - # Added: BLB	- added for store requirements		Jul 2, 2017
	#prev. ver. - DisplayStoreOutput (numTiresStore, totalCostStore)

	#Display all customer info and  Store totals output - # Added: BLB	- added for array requirements		Jul 22, 2017
	DisplayCustStoreTotals (custNames, custAddrs, custTires, custCosts)

#--- Execute -----------------------------------------------
main()
