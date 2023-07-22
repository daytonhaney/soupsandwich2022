
try:
    numerator = int(input("Enter number to divide: "))
    demom = int(input("Enter number to divide: "))
    result = numerator / demom
    print(result)

except Exception:
    print("Sorry, try again:")
except ValueError:
    print("Please try agaiddn")



