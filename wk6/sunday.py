intro_msg = "You had several very busy weeks, and you have taken a lot of tests\nYou have an idea of the grades you received, but you want a more accurate guesstimation...\n\nPlease enter grades, use comma ',' between entries, hit enter/return when finished\n\nYou will receive an average of the grades you input."
print("-"*35, "Welcome", "To", "Quick", "Guess", "-"*34, sep="*")
print("\n             ------ A tool that quickly returns the average of a string.-----")
print('')
print('')
print(intro_msg)
test_scores = list(
    map(int, input("  \nTest Scores you wish to find average:  ").split(",")))
print("\n\n Your test scores are : ", test_scores)


def get_average(test_scores):
    result = len(test_scores) / sum(test_scores)
    print(result)


get_average(test_scores)
