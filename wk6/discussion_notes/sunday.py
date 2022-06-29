intro_msg = "You are in college and you have days that are busy,\nSometimes you need to quickly get average of grades..."


print("-"*35, "Welcome", "To", "Quick", "Guess", "-"*34, sep="*")  # using spring primitives to build designs
print("\n             ------ A tool that quickly returns the average of a string.-----")
print('')
print('')
print(intro_msg.center(50))
test_scores = list(
    map(int, input("  \nTest Scores you wish to find average:  ").split(","))) # Using map because it is faster than \list comprehension for a single argument

#
print("\n\n Your test scores are : ", test_scores)


def get_average(test_scores):
    result = sum(test_scores) / len(test_scores)
    print(result)


get_average(test_scores)
